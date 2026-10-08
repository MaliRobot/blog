/*
 * Drag & drop reordering for the Šuško sections changelist.
 *
 * The rows of the changelist become draggable; dropping a row sends the new
 * order to the admin "reorder/" view. The `order` column stays editable, so
 * everything still works when JavaScript is disabled.
 */
(function () {
    "use strict";

    function getCookie(name) {
        var cookies = (document.cookie || "").split(";");

        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();

            if (cookie.indexOf(name + "=") === 0) {
                return decodeURIComponent(cookie.substring(name.length + 1));
            }
        }

        return "";
    }

    function rowId(row) {
        var checkbox = row.querySelector('input[name="_selected_action"]');
        return checkbox ? checkbox.value : null;
    }

    function collectIds(tbody) {
        var ids = [];

        tbody.querySelectorAll("tr").forEach(function (row) {
            var id = rowId(row);

            if (id) {
                ids.push(id);
            }
        });

        return ids;
    }

    function renumberOrderInputs(tbody) {
        var position = 1;

        tbody.querySelectorAll("tr").forEach(function (row) {
            var input = row.querySelector('input[name$="-order"]');

            if (input) {
                input.value = position;
            }

            position += 1;
        });
    }

    function save(tbody, statusNode) {
        var ids = collectIds(tbody);

        fetch(window.location.pathname + "reorder/", {
            method: "POST",
            credentials: "same-origin",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
                "X-Requested-With": "XMLHttpRequest"
            },
            body: JSON.stringify({ ids: ids })
        })
            .then(function (response) {
                if (!response.ok) {
                    throw new Error("Reordering failed");
                }
                return response.json();
            })
            .then(function () {
                renumberOrderInputs(tbody);
                statusNode.textContent = "New order saved.";
            })
            .catch(function () {
                statusNode.textContent =
                    "Could not save the new order, please reload the page.";
            });
    }

    document.addEventListener("DOMContentLoaded", function () {
        var table = document.getElementById("result_list");

        if (!table) {
            return;
        }

        var tbody = table.querySelector("tbody");

        if (!tbody) {
            return;
        }

        var statusNode = document.createElement("p");
        statusNode.className = "susko-reorder-help";
        statusNode.textContent = "Tip: drag the rows to reorder the sections.";
        table.parentNode.insertBefore(statusNode, table);

        var dragged = null;

        tbody.querySelectorAll("tr").forEach(function (row) {
            if (!rowId(row)) {
                return;
            }

            row.setAttribute("draggable", "true");
            row.style.cursor = "move";

            row.addEventListener("dragstart", function () {
                dragged = row;
                row.style.opacity = "0.4";
            });

            row.addEventListener("dragend", function () {
                row.style.opacity = "";
            });

            row.addEventListener("dragover", function (event) {
                event.preventDefault();
            });

            row.addEventListener("drop", function (event) {
                event.preventDefault();

                if (!dragged || dragged === row) {
                    return;
                }

                var rows = Array.prototype.slice.call(tbody.querySelectorAll("tr"));

                if (rows.indexOf(dragged) < rows.indexOf(row)) {
                    row.parentNode.insertBefore(dragged, row.nextSibling);
                } else {
                    row.parentNode.insertBefore(dragged, row);
                }

                dragged = null;
                save(tbody, statusNode);
            });
        });
    });
})();