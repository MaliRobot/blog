-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 08, 2023 at 09:27 PM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nonlinear`
--

-- --------------------------------------------------------

--
-- Table structure for table `about`
--

CREATE TABLE IF NOT EXISTS `about` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `about`
--

INSERT INTO `about` (`id`, `text`) VALUES
(1, 'I should be me.');

-- --------------------------------------------------------

--
-- Table structure for table `access_logs`
--

CREATE TABLE IF NOT EXISTS `access_logs` (
  `sys_id` int(11) NOT NULL AUTO_INCREMENT,
  `session_key` varchar(1024) NOT NULL,
  `path` varchar(1024) NOT NULL,
  `method` varchar(8) NOT NULL,
  `data` longtext,
  `ip_address` varchar(45) NOT NULL,
  `referrer` varchar(512) DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`sys_id`)
) ENGINE=InnoDB AUTO_INCREMENT=877 DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Table structure for table `admin_interface_theme`
--

CREATE TABLE IF NOT EXISTS `admin_interface_theme` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `title` varchar(50) NOT NULL,
  `title_visible` tinyint(1) NOT NULL,
  `logo` varchar(100) NOT NULL,
  `logo_visible` tinyint(1) NOT NULL,
  `css_header_background_color` varchar(10) NOT NULL,
  `title_color` varchar(10) NOT NULL,
  `css_header_text_color` varchar(10) NOT NULL,
  `css_header_link_color` varchar(10) NOT NULL,
  `css_header_link_hover_color` varchar(10) NOT NULL,
  `css_module_background_color` varchar(10) NOT NULL,
  `css_module_text_color` varchar(10) NOT NULL,
  `css_module_link_color` varchar(10) NOT NULL,
  `css_module_link_hover_color` varchar(10) NOT NULL,
  `css_module_rounded_corners` tinyint(1) NOT NULL,
  `css_generic_link_color` varchar(10) NOT NULL,
  `css_generic_link_hover_color` varchar(10) NOT NULL,
  `css_save_button_background_color` varchar(10) NOT NULL,
  `css_save_button_background_hover_color` varchar(10) NOT NULL,
  `css_save_button_text_color` varchar(10) NOT NULL,
  `css_delete_button_background_color` varchar(10) NOT NULL,
  `css_delete_button_background_hover_color` varchar(10) NOT NULL,
  `css_delete_button_text_color` varchar(10) NOT NULL,
  `css` longtext NOT NULL,
  `list_filter_dropdown` tinyint(1) NOT NULL,
  `related_modal_active` tinyint(1) NOT NULL,
  `related_modal_background_color` varchar(10) NOT NULL,
  `related_modal_rounded_corners` tinyint(1) NOT NULL,
  `logo_color` varchar(10) NOT NULL,
  `recent_actions_visible` tinyint(1) NOT NULL,
  `favicon` varchar(100) NOT NULL,
  `related_modal_background_opacity` varchar(5) NOT NULL,
  `env_name` varchar(50) NOT NULL,
  `env_visible_in_header` tinyint(1) NOT NULL,
  `env_color` varchar(10) NOT NULL,
  `env_visible_in_favicon` tinyint(1) NOT NULL,
  `related_modal_close_button_visible` tinyint(1) NOT NULL,
  `language_chooser_active` tinyint(1) NOT NULL,
  `language_chooser_display` varchar(10) NOT NULL,
  `list_filter_sticky` tinyint(1) NOT NULL,
  `form_pagination_sticky` tinyint(1) NOT NULL,
  `form_submit_sticky` tinyint(1) NOT NULL,
  `css_module_background_selected_color` varchar(10) NOT NULL,
  `css_module_link_selected_color` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_interface_theme_name_30bda70f_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `admin_interface_theme`
--

INSERT INTO `admin_interface_theme` (`id`, `name`, `active`, `title`, `title_visible`, `logo`, `logo_visible`, `css_header_background_color`, `title_color`, `css_header_text_color`, `css_header_link_color`, `css_header_link_hover_color`, `css_module_background_color`, `css_module_text_color`, `css_module_link_color`, `css_module_link_hover_color`, `css_module_rounded_corners`, `css_generic_link_color`, `css_generic_link_hover_color`, `css_save_button_background_color`, `css_save_button_background_hover_color`, `css_save_button_text_color`, `css_delete_button_background_color`, `css_delete_button_background_hover_color`, `css_delete_button_text_color`, `css`, `list_filter_dropdown`, `related_modal_active`, `related_modal_background_color`, `related_modal_rounded_corners`, `logo_color`, `recent_actions_visible`, `favicon`, `related_modal_background_opacity`, `env_name`, `env_visible_in_header`, `env_color`, `env_visible_in_favicon`, `related_modal_close_button_visible`, `language_chooser_active`, `language_chooser_display`, `list_filter_sticky`, `form_pagination_sticky`, `form_submit_sticky`, `css_module_background_selected_color`, `css_module_link_selected_color`) VALUES
(1, 'Django', 1, 'Django administration', 1, '', 1, '#0C4B33', '#F5DD5D', '#44B78B', '#FFFFFF', '#C9F0DD', '#44B78B', '#FFFFFF', '#FFFFFF', '#C9F0DD', 1, '#0C3C26', '#156641', '#0C4B33', '#0C3C26', '#FFFFFF', '#BA2121', '#A41515', '#FFFFFF', '', 1, 1, '#000000', 1, '#FFFFFF', 1, '', '0.3', '', 1, '#E74C3C', 1, 1, 1, 'code', 1, 0, 0, '#FFFFCC', '#FFFFFF');

-- --------------------------------------------------------

--
-- Table structure for table `albums`
--

CREATE TABLE IF NOT EXISTS `albums` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `artist` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `code` varchar(12) NOT NULL,
  `release_date` date NOT NULL,
  `public` tinyint(1) NOT NULL,
  `image_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `albums_image_id_5e8a0206_fk_images_id` (`image_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add about', 1, 'add_about'),
(2, 'Can change about', 1, 'change_about'),
(3, 'Can delete about', 1, 'delete_about'),
(4, 'Can view about', 1, 'view_about'),
(5, 'Can add album', 2, 'add_album'),
(6, 'Can change album', 2, 'change_album'),
(7, 'Can delete album', 2, 'delete_album'),
(8, 'Can view album', 2, 'view_album'),
(9, 'Can add event', 3, 'add_event'),
(10, 'Can change event', 3, 'change_event'),
(11, 'Can delete event', 3, 'delete_event'),
(12, 'Can view event', 3, 'view_event'),
(13, 'Can add image', 4, 'add_image'),
(14, 'Can change image', 4, 'change_image'),
(15, 'Can delete image', 4, 'delete_image'),
(16, 'Can view image', 4, 'view_image'),
(17, 'Can add news', 5, 'add_news'),
(18, 'Can change news', 5, 'change_news'),
(19, 'Can delete news', 5, 'delete_news'),
(20, 'Can view news', 5, 'view_news'),
(21, 'Can add poem', 6, 'add_poem'),
(22, 'Can change poem', 6, 'change_poem'),
(23, 'Can delete poem', 6, 'delete_poem'),
(24, 'Can view poem', 6, 'view_poem'),
(25, 'Can add post', 7, 'add_post'),
(26, 'Can change post', 7, 'change_post'),
(27, 'Can delete post', 7, 'delete_post'),
(28, 'Can view post', 7, 'view_post'),
(29, 'Can add comment', 8, 'add_comment'),
(30, 'Can change comment', 8, 'change_comment'),
(31, 'Can delete comment', 8, 'delete_comment'),
(32, 'Can view comment', 8, 'view_comment'),
(33, 'Can add access log', 9, 'add_accesslog'),
(34, 'Can change access log', 9, 'change_accesslog'),
(35, 'Can delete access log', 9, 'delete_accesslog'),
(36, 'Can view access log', 9, 'view_accesslog'),
(37, 'Can add log entry', 10, 'add_logentry'),
(38, 'Can change log entry', 10, 'change_logentry'),
(39, 'Can delete log entry', 10, 'delete_logentry'),
(40, 'Can view log entry', 10, 'view_logentry'),
(41, 'Can add permission', 11, 'add_permission'),
(42, 'Can change permission', 11, 'change_permission'),
(43, 'Can delete permission', 11, 'delete_permission'),
(44, 'Can view permission', 11, 'view_permission'),
(45, 'Can add group', 12, 'add_group'),
(46, 'Can change group', 12, 'change_group'),
(47, 'Can delete group', 12, 'delete_group'),
(48, 'Can view group', 12, 'view_group'),
(49, 'Can add user', 13, 'add_user'),
(50, 'Can change user', 13, 'change_user'),
(51, 'Can delete user', 13, 'delete_user'),
(52, 'Can view user', 13, 'view_user'),
(53, 'Can add content type', 14, 'add_contenttype'),
(54, 'Can change content type', 14, 'change_contenttype'),
(55, 'Can delete content type', 14, 'delete_contenttype'),
(56, 'Can view content type', 14, 'view_contenttype'),
(57, 'Can add session', 15, 'add_session'),
(58, 'Can change session', 15, 'change_session'),
(59, 'Can delete session', 15, 'delete_session'),
(60, 'Can view session', 15, 'view_session'),
(61, 'Can add Tag', 16, 'add_tag'),
(62, 'Can change Tag', 16, 'change_tag'),
(63, 'Can delete Tag', 16, 'delete_tag'),
(64, 'Can view Tag', 16, 'view_tag'),
(65, 'Can add Tagged Item', 17, 'add_taggeditem'),
(66, 'Can change Tagged Item', 17, 'change_taggeditem'),
(67, 'Can delete Tagged Item', 17, 'delete_taggeditem'),
(68, 'Can view Tagged Item', 17, 'view_taggeditem'),
(69, 'Can add contact', 18, 'add_contact'),
(70, 'Can change contact', 18, 'change_contact'),
(71, 'Can delete contact', 18, 'delete_contact'),
(72, 'Can view contact', 18, 'view_contact'),
(73, 'Can add Theme', 19, 'add_theme'),
(74, 'Can change Theme', 19, 'change_theme'),
(75, 'Can delete Theme', 19, 'delete_theme'),
(76, 'Can view Theme', 19, 'view_theme');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$120000$ErN7xO2bK0aQ$WIRUd1M50lmacQLNp74b1AIxvYyvNv+y0q64Z2NNUpg=', '2020-12-27 12:43:15.130501', 1, 'malirobot', '', '', 'milos.trifunovic@gmail.com', 1, 1, '2019-11-17 21:37:07.009333');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE IF NOT EXISTS `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `text` longtext NOT NULL,
  `author` varchar(255) NOT NULL,
  `public` tinyint(1) NOT NULL,
  `date_posted` datetime(6) NOT NULL,
  `post_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `comments_post_id_67cfce36_fk_posts_id` (`post_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE IF NOT EXISTS `contacts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`id`, `subject`, `email`, `message`) VALUES
(1, 'test', 'milos.trifunovic@gmail.com', 'test'),
(2, 'Python Developer', 'milos.trifunovic@gmail.com', 'opa');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=492 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(489, '2020-11-23 18:21:35.127728', '2', 'Review: One they bands in my neighborhood', 2, '[{\"changed\": {\"fields\": [\"tags\"]}}]', 7, 1),
(490, '2020-11-23 22:09:36.553955', '11', 'Tour de Misha', 1, '[{\"added\": {}}]', 5, 1),
(491, '2020-11-30 12:32:17.722441', '1', 'Digital Prayer at Speculum Atrium', 2, '[{\"changed\": {\"fields\": [\"address\", \"city\", \"location\"]}}]', 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'about', 'about'),
(18, 'about', 'contact'),
(9, 'access_log', 'accesslog'),
(10, 'admin', 'logentry'),
(19, 'admin_interface', 'theme'),
(2, 'albums', 'album'),
(12, 'auth', 'group'),
(11, 'auth', 'permission'),
(13, 'auth', 'user'),
(14, 'contenttypes', 'contenttype'),
(3, 'events', 'event'),
(4, 'images', 'image'),
(5, 'news', 'news'),
(6, 'poems', 'poem'),
(8, 'posts', 'comment'),
(7, 'posts', 'post'),
(15, 'sessions', 'session'),
(16, 'taggit', 'tag'),
(17, 'taggit', 'taggeditem');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'about', '0001_initial', '2020-11-23 13:11:08.202135'),
(2, 'access_log', '0001_initial', '2020-11-23 13:11:33.128031'),
(3, 'contenttypes', '0001_initial', '2020-11-23 13:11:43.898369'),
(4, 'auth', '0001_initial', '2020-11-23 13:13:17.403121'),
(5, 'admin', '0001_initial', '2020-11-23 13:13:48.202722'),
(6, 'admin', '0002_logentry_remove_auto_add', '2020-11-23 13:13:48.226610'),
(7, 'admin', '0003_logentry_add_action_flag_choices', '2020-11-23 13:13:48.254916'),
(8, 'images', '0001_initial', '2020-11-23 13:13:58.437910'),
(9, 'albums', '0001_initial', '2020-11-23 13:14:30.777823'),
(10, 'contenttypes', '0002_remove_content_type_name', '2020-11-23 13:14:31.078862'),
(11, 'auth', '0002_alter_permission_name_max_length', '2020-11-23 13:14:31.242813'),
(12, 'auth', '0003_alter_user_email_max_length', '2020-11-23 13:14:31.370866'),
(13, 'auth', '0004_alter_user_username_opts', '2020-11-23 13:14:31.402633'),
(14, 'auth', '0005_alter_user_last_login_null', '2020-11-23 13:14:31.518839'),
(15, 'auth', '0006_require_contenttypes_0002', '2020-11-23 13:14:31.532015'),
(16, 'auth', '0007_alter_validators_add_error_messages', '2020-11-23 13:14:31.563023'),
(17, 'auth', '0008_alter_user_username_max_length', '2020-11-23 13:14:31.718765'),
(18, 'auth', '0009_alter_user_last_name_max_length', '2020-11-23 13:14:31.886739'),
(19, 'events', '0001_initial', '2020-11-23 13:15:51.082801'),
(20, 'news', '0001_initial', '2020-11-23 13:16:31.575264'),
(21, 'poems', '0001_initial', '2020-11-23 13:17:10.524709'),
(22, 'taggit', '0001_initial', '2020-11-23 13:17:44.866710'),
(23, 'taggit', '0002_auto_20150616_2121', '2020-11-23 13:17:44.957219'),
(24, 'taggit', '0003_taggeditem_add_unique_index', '2020-11-23 13:17:45.054779'),
(25, 'posts', '0001_initial', '2020-11-23 13:18:53.962702'),
(26, 'sessions', '0001_initial', '2020-11-23 13:19:00.351334'),
(27, 'about', '0002_auto_20201124_1718', '2020-11-24 16:44:45.247534'),
(28, 'events', '0002_auto_20201124_1522', '2020-11-24 16:44:45.275505'),
(29, 'images', '0002_auto_20201124_1610', '2020-11-24 16:44:45.307416'),
(30, 'posts', '0002_auto_20201124_1522', '2020-11-24 16:44:45.527544'),
(31, 'posts', '0003_auto_20201124_1610', '2020-11-24 16:44:45.571736'),
(32, 'about', '0003_contact', '2020-11-27 16:26:51.882611'),
(33, 'admin_interface', '0001_initial', '2020-11-27 16:32:09.934401'),
(34, 'admin_interface', '0002_add_related_modal', '2020-11-27 16:33:00.750308'),
(35, 'admin_interface', '0003_add_logo_color', '2020-11-27 16:33:11.096772'),
(36, 'admin_interface', '0004_rename_title_color', '2020-11-27 16:33:11.151659'),
(37, 'admin_interface', '0005_add_recent_actions_visible', '2020-11-27 16:33:19.608667'),
(38, 'admin_interface', '0006_bytes_to_str', '2020-11-27 16:33:19.720810'),
(39, 'admin_interface', '0007_add_favicon', '2020-11-27 16:33:27.954253'),
(40, 'admin_interface', '0008_change_related_modal_background_opacity_type', '2020-11-27 16:33:40.820122'),
(41, 'admin_interface', '0009_add_enviroment', '2020-11-27 16:34:02.386918'),
(42, 'admin_interface', '0010_add_localization', '2020-11-27 16:34:02.430355'),
(43, 'admin_interface', '0011_add_environment_options', '2020-11-27 16:34:22.578254'),
(44, 'admin_interface', '0012_update_verbose_names', '2020-11-27 16:34:22.606147'),
(45, 'admin_interface', '0013_add_related_modal_close_button', '2020-11-27 16:34:30.126379'),
(46, 'admin_interface', '0014_name_unique', '2020-11-27 16:34:30.206351'),
(47, 'admin_interface', '0015_add_language_chooser_active', '2020-11-27 16:34:40.942348'),
(48, 'admin_interface', '0016_add_language_chooser_display', '2020-11-27 16:34:45.287009'),
(49, 'admin_interface', '0017_change_list_filter_dropdown', '2020-11-27 16:34:45.318026'),
(50, 'admin_interface', '0018_theme_list_filter_sticky', '2020-11-27 16:34:50.514329'),
(51, 'admin_interface', '0019_add_form_sticky', '2022-05-03 12:36:18.824007'),
(52, 'admin_interface', '0020_module_selected_colors', '2022-05-03 12:36:19.004715'),
(53, 'admin_interface', '0021_file_extension_validator', '2022-05-03 12:36:19.014684'),
(54, 'auth', '0010_alter_group_name_max_length', '2022-05-03 12:36:19.089047'),
(55, 'auth', '0011_update_proxy_permissions', '2022-05-03 12:36:19.109079'),
(56, 'auth', '0012_alter_user_first_name_max_length', '2022-05-03 12:36:19.172547'),
(57, 'posts', '0004_alter_post_text', '2022-05-03 12:36:19.184075');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('04ol50aqkryx57descnfk6qflefd88p6', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-11-30 01:39:09.285316'),
('0s0ni99amp5o5721ty0cacwfm1l8p82r', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 20:55:37.903076'),
('0u653uqa597njklbqu5ptao6uzkppup5', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-22 22:46:48.588065'),
('1dd0df7nhvaikiicwrbe8su5hc48z6x9', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 23:59:02.875953'),
('1e84d0me8ajxcyow3ss1zvopmmz10alx', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-28 02:28:34.572660'),
('1koqek3nz1i37drd01jgr3p22bq6d8ag', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-27 23:53:42.415580'),
('1s7b4yuwl3abw6xsdq9splfrigls6blf', 'e30:1nlrmY:r8teC6UQl0sYJ4F-bRL0JXWVFlzZTem7oNedx0T88Yk', '2022-05-17 12:37:34.800309'),
('255r73ov6pii8ml8890atckhhokar565', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 16:44:24.598527'),
('2gytoohoixzyhfg61s0atbe5zkzremda', 'YTMwNzk3YWNmYmMwMzVkYTJkZDg5ZGE5OTg3OGM2NDI3N2Y3ZGQyNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzMDAyYzRiYzk5NTdmZDJhYTkyMDI4MzljN2FlODY1N2FlYWFlNzQyIn0=', '2020-10-24 16:31:49.506258'),
('2ibyx147m0smju0df5ti6legge0r9caj', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:25:52.338140'),
('2nfd55yceqsg85clceqm45cl4uizcccd', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 20:55:45.868523'),
('324k9ifs8yqsn69yikdpuqrhnqgglah2', 'YTFhMzM2ZjYyODk2ZGQzYTMzNTE4NTEwODQ0NDRiMGRmNjA4ZGI1OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxNDRiOGRjOTYyMDg3MWM5OWJmZDU0Njg2ODk5ZDM4OTNmNmUzY2NlIn0=', '2020-06-28 20:57:41.326041'),
('3hfbct4fm2w0vhs2mhkgp9zvgdpn43ze', 'e30:1nlrmy:gtk7cQf3PiDLMKBdY6L2kJKZwHO79RPoTa8IcXB6xM4', '2022-05-17 12:38:00.789307'),
('3jagl2c1uldywnpo4sl2qjwvk5j6wsy3', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 20:55:42.860525'),
('3pebjx8eqm8z8qsotx3pm8qxzfi6v8er', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-09 12:47:19.516797'),
('44uhlj9ua84uotnswx4d3tm4p0gh53le', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 17:34:58.602587'),
('4dr2cuqe6zzyznxz0hxdgto20wx2x9lh', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2021-01-07 00:10:22.866765'),
('4ilubnydstcysi65jqs4tczhcde0pdts', 'YTFhMzM2ZjYyODk2ZGQzYTMzNTE4NTEwODQ0NDRiMGRmNjA4ZGI1OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxNDRiOGRjOTYyMDg3MWM5OWJmZDU0Njg2ODk5ZDM4OTNmNmUzY2NlIn0=', '2020-03-15 20:28:27.045918'),
('4okavk2bocjw76tz9jqj0grsysl26ysq', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 20:55:42.624558'),
('4v3gpqlnbrt63tpzct6n8c4ya0xaqm2f', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 20:55:36.092289'),
('53yukydcf4jvk3y2outwukv1rzltt2xo', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 12:16:51.005013'),
('56aaphp4kppj482i1asbktfrbnl6iatl', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-27 20:37:26.627298'),
('5anbz1wnscacjwv9jdv44i4uk1bhezyc', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 17:47:45.190933'),
('5e5pbcyd51v9igt5nzzeoegxmuzwqrmw', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2021-01-08 15:43:01.483841'),
('5i3twwirmyekrbli3qkcazvaucsx37g1', 'e30:1nlrkw:LBeVKGXUxkivaCaluhpi8TOJ-69_9gS0ltA4OrPnGlY', '2022-05-17 12:35:54.327852'),
('5vtvqoojpe2zjgijz872wtnw8u5ikzfy', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:26:17.730099'),
('5vxuwwns54m7wymyfufx0a1bje1p0vpy', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-11-30 01:39:09.239817'),
('6b88x01dbf8mwfm8znbpdh5019b1t41m', 'YTFhMzM2ZjYyODk2ZGQzYTMzNTE4NTEwODQ0NDRiMGRmNjA4ZGI1OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxNDRiOGRjOTYyMDg3MWM5OWJmZDU0Njg2ODk5ZDM4OTNmNmUzY2NlIn0=', '2019-12-01 21:43:25.096725'),
('6oozow05txgc9831dwv9x0zxgm69zcby', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 20:55:40.952545'),
('7tbmas9pu426zxz57i5beof7pnr7pt5p', 'e30:1nlrn0:xGkHBduXqA_Ffu128xjXKYE9wxA81MRIXqFfA8wKB5w', '2022-05-17 12:38:02.682535'),
('89ao92huegmr83znz7ocqb0lp0lxpiam', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2021-01-08 14:59:33.435776'),
('89v8c4qlnixk4gzfd3rdag2rxeffz9ry', 'OWM3YWQyMTY5YTAxODA5Y2RhZDY5M2NjNWZiNjcyZDFhYTczOTk5YTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMDEwN2ZhYzRiYWY1OTYwNjQyYTg5NGI5NjJhMmY1NWFmMzhmZTAwIn0=', '2020-11-30 01:41:02.207513'),
('8ci7sqz7y3pksyfv4nztov85z1p6dboc', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-12 03:03:56.746862'),
('8crkbgsh3nyn8ck3gcwaexx3u10uimiq', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:20:38.118313'),
('8k2hcdvqxerb7qk6luzsbrei8ceueo9i', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-27 22:21:54.454628'),
('8wbf1kcxh31nfslsd73s2wl3hq81e3aj', 'e30:1nlrkm:rv4kXgKL9z8DlTZSuisXdeKuY26quYu6GJXOMZ0FeHE', '2022-05-17 12:35:44.383584'),
('981ylbxac8ifcmkd5tr05ar0ug38fjrs', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:25:21.358048'),
('9c1soripsi0838v1ois5ag16ny8zzytg', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:20:36.902554'),
('9e41ll4xshsv77rqw25ljtox6gzgglmt', 'e30:1nlrmA:bepXu5-PNRKGbPF7gip3v-UEFM-EKWnWLX9AHLAPWLQ', '2022-05-17 12:37:10.164944'),
('a9wd0mgdm6u3zvun3d8hvhj67mxihzol', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-19 11:09:08.576185'),
('acnqvxp38byrllaerjtc3aiggdd0jqgy', 'YTFhMzM2ZjYyODk2ZGQzYTMzNTE4NTEwODQ0NDRiMGRmNjA4ZGI1OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxNDRiOGRjOTYyMDg3MWM5OWJmZDU0Njg2ODk5ZDM4OTNmNmUzY2NlIn0=', '2020-05-27 22:08:29.865768'),
('ag2hcfj373qjj7jaw8nyl2v67hazmltx', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-27 21:47:16.855654'),
('alwb3divtyixv4xbqukio6aw5zl0nbpq', 'NzEwZDcwNDZkZTMyZTY3NDBmZWFmNTQyMzM0N2U1NGYxYjNmZmM5YTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhY2QwNTA2N2ZiZGE3YzIwN2NkNGQ4NzNlM2MwZWJkODc2NWJiZTVlIn0=', '2020-12-07 17:48:08.490906'),
('ar0ykaq0xb0cboa6tbrt94bn3r4p4urf', 'YTFhMzM2ZjYyODk2ZGQzYTMzNTE4NTEwODQ0NDRiMGRmNjA4ZGI1OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxNDRiOGRjOTYyMDg3MWM5OWJmZDU0Njg2ODk5ZDM4OTNmNmUzY2NlIn0=', '2019-12-04 21:54:29.962182'),
('asz6pat3ncudr6nu3zfo8zv7qq7gokvs', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:25:52.991821'),
('atgiw2m3fr1ed78vx06b9tzh0ctnagh4', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 23:59:02.883625'),
('b9mht6de6i9pa2idns9lw4em1mdxqxg5', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:24:05.964038'),
('bb7wxzdyam0i04838g70hneatao9q79k', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:20:34.618412'),
('bd0zb2bad2tzcdxthaopprvayg6x2jp6', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 20:55:43.448502'),
('bu9vci5rgtipwe9vz9yr24f18vz9y7ck', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 20:55:36.052590'),
('c4i4s4os3x19eyyqps363rga3rym1s1m', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:26:54.690796'),
('c6jle1z4xqfulxjc89k4qsqd5tjdw88n', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2021-01-03 21:46:31.276402'),
('c7ow3e9jrf6ptyom2thgqtefggazyslw', 'e30:1nlrmW:bqIhbsODJVlLCFsafHcz9seUXvUfxfRU3u_2F2SPoNI', '2022-05-17 12:37:32.132315'),
('c8vkefu7xv85qkp0bzu7tryux8sxucsu', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:20:36.229381'),
('cdh0sg7qrdf44rie1pd0hmd816z7h05j', 'NzEwZDcwNDZkZTMyZTY3NDBmZWFmNTQyMzM0N2U1NGYxYjNmZmM5YTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhY2QwNTA2N2ZiZGE3YzIwN2NkNGQ4NzNlM2MwZWJkODc2NWJiZTVlIn0=', '2021-01-10 12:43:15.138127'),
('cr1bckbsiesrty335dz09xefnc14iuk9', 'NzEwZDcwNDZkZTMyZTY3NDBmZWFmNTQyMzM0N2U1NGYxYjNmZmM5YTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhY2QwNTA2N2ZiZGE3YzIwN2NkNGQ4NzNlM2MwZWJkODc2NWJiZTVlIn0=', '2020-12-22 22:47:18.617745'),
('cr5irjox8xn23h1ts0szzh5n0zs2o8qk', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:25:57.226196'),
('cy8o3ru4y5ny4ryaiek3x80bapwlhoj4', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 20:55:43.192458'),
('d9hcmvx2ace8huhxlpj59elyk5admeux', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-19 16:31:35.843118'),
('dc6z8xol8gyt74fqqy4inh7p579yjai0', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2021-01-07 00:40:31.627714'),
('ddvgemngjkg3adwo7rd82hxv9qmx33dq', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-27 20:37:25.615331'),
('dii0zfctljg5j8smmsyripayrxu67pxx', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 14:02:05.905947'),
('e628s8nvhuie1ofdwov22jsy6jq7sc51', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-20 12:24:37.711275'),
('e6zetkvl30u426reun885vjo2w10ghcp', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 23:59:03.533303'),
('enjrzlr670weeszjjk4zey0jcv6zuuww', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:25:53.882924'),
('esvf1il72fsqriv5s21ifvu4hnivfaad', 'e30:1nlrkl:mLrdCinqVRQZlgP2QwYZjQ1xG7935UFXMV8xSJDhKE4', '2022-05-17 12:35:43.989084'),
('eykkhhuzritmmdl8adllcetya0g19t84', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-24 19:56:21.245712'),
('f8exedw30tv36xkpclxbcqylc1c94b79', 'e30:1lkwt8:JkPxKCjQ-thmLHG-F7ALzjJk_Rnk4kAN2DanBf4NAfw', '2021-06-06 22:48:02.256348'),
('gmziedjywjelyc7b787mfkpr0i9o1aj0', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:26:46.350151'),
('gyh6htckcvoljwkd4dy51j1tmuzgbqo2', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 17:05:47.374320'),
('h79han1xm466te3u6douu8c81wc5f5ur', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 20:55:35.172601'),
('hg00jxj3q4wnkakooozw3pzherwky7y2', 'e30:1nlrn2:WZz0bXo5wx4oQgSRopdH4L4AY6Z9xGGTa-vBUgUSBOQ', '2022-05-17 12:38:04.115734'),
('hgfbabblprk7t8qu63m3sy9km0gxoha2', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2021-01-17 00:20:52.907806'),
('i2mu4vmswr4jd9dr18egxcryk9wfyh5r', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:26:52.794672'),
('i9um4pfr8a093f9d9zu48t8k0qscrjlq', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-27 21:12:43.883204'),
('iplsiqpp7oezqirazagne9h5ukrah4ek', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2021-01-14 09:50:12.800211'),
('ivj96sj17xu2t5nftff6im3yonv0vfbj', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-19 13:30:52.245001'),
('jd5yvqayfaaarhn3hp4cmqnrt2478nkj', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 20:55:48.227760'),
('jlfuk3f3dl45vj8wpchw29itob18r8z4', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 20:55:33.616761'),
('k6fzvybpjptzg2vyn2ri7nh7wpeaov0m', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 16:59:34.510145'),
('khu67ri0wymioi99abri9etjlvvvqa0j', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-11 11:59:25.065981'),
('kqwc6b0mh58mcccri525s3ff0i5uuirp', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:25:53.773566'),
('m8hiw5mvuvxo9vp0p1xoplg1zaih2y28', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:20:33.990984'),
('mmh0tqeh9w7wzlk09w0s49uynxsn1f11', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:20:37.822133'),
('mmpz953g434kgghhcn0483dk8da7iu98', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:20:36.234268'),
('motnuvjyeyy6wkvwv49fyrt7wft3ckae', 'YTFhMzM2ZjYyODk2ZGQzYTMzNTE4NTEwODQ0NDRiMGRmNjA4ZGI1OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxNDRiOGRjOTYyMDg3MWM5OWJmZDU0Njg2ODk5ZDM4OTNmNmUzY2NlIn0=', '2020-04-17 19:56:38.143593'),
('n62xivt07i09qu1oe6jz10ghix7quhct', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-10 16:26:12.398665'),
('ngx9z6s6a8u70joojjaiqi2kglgb2em3', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:25:19.171433'),
('nj9s57dcnn98m2c0usuu2ualtja2zeav', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-28 00:24:21.401117'),
('nnj0dy1llnhdl5zgixm7gyql6z2yb9rh', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-21 13:04:43.394614'),
('np0flfkxajkvjn7isz14ib6il71auloj', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-27 22:52:10.524701'),
('opvx37iep891sht48usmyr4wf0ro0eu5', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 20:55:34.276944'),
('oro0uocei4hc28e8cpvm0qtxjrf88e6s', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:25:52.586039'),
('p2nb5y1n0xjevvme87bmp7vk2aajmc02', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:26:56.481582'),
('q4ysuumkv637d4u5zp33anl8fmn1jwsi', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:20:37.858410'),
('q8o7t2bfs6c704nr8rm6b81sqg8oq82g', 'e30:1nlrnU:kFYsGPRWRJwaynv7wRIHDurk0ZtIAgIAGb6nSNKx9KU', '2022-05-17 12:38:32.582429'),
('q9idpm5qev5361nx3ubm4cj0z961nino', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2021-01-09 01:05:14.925564'),
('qdjqsf6dgy650218v8erecxitk1ocvzz', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:25:18.785481'),
('qs3vy527ldhk79xz12kehgwkswnbc94c', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 16:54:27.213617'),
('qtjpenfbgjyrgr0csnqpluygl6oltsg2', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2021-01-15 22:37:41.766019'),
('qu8c5e5s9cy02p5vdgfmujk7k1keifpz', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2021-01-08 15:43:03.099859'),
('r7leb8q8wrweqo0qdunsf0x8flsoy5r1', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:25:53.214086'),
('rdkcektdjo6b0u9a24637a3p3vz5po9c', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-09 12:47:19.721968'),
('rv8oh21ug79mozc7k9pkzax06b7tstap', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-11-30 01:39:09.262816'),
('s6bmefcl96nz1nch8lwmlajw1lhh8fd6', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-27 20:37:31.964823'),
('s9xhbar8pp2cxrvxxh5x3b5lvumqxf88', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2021-01-14 09:53:46.788419'),
('sa7qjjbc441qs6453c442dor1thnsfmf', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:20:33.998232'),
('t2t7firmofofyaaufcvg8q75q9m8a8g7', 'e30:1nlrmU:2Ade8AXs2Jg302XZq_2OoiUADwkCvmqwUU6haugykyw', '2022-05-17 12:37:30.474485'),
('t34avk331m4vojbfvme94jqlmz2lgr51', 'e30:1nlrmZ:ch6nj5lFYrj6cwHGCJUmALauXryL8S9tacZCUwkmn6k', '2022-05-17 12:37:35.596761'),
('tskesv4ninaate2wl91va9e1wql1qcbc', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-09 12:47:20.095394'),
('u04quhycxxel22at4dzofj5rwxlgb95e', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-27 23:22:36.983393'),
('uaexwmgxxyevb3n5fpka83szwt39xkag', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:26:01.510232'),
('uirnzxaxv050gl7r0i2vcvfgtw561yvx', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2021-01-18 16:17:30.002226'),
('vxvdbubygj53rdthi8s8eeuwe5pqstm1', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 20:55:39.228651'),
('vy7fwm4i1oga61k560fj0e1r4za8ohws', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 20:55:41.508682'),
('wa5c2smluypuqdcfgvgbgzope8vsk3zw', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:20:36.864257'),
('we5wob508zph9v74c70okotqvsdio10a', 'YTFhMzM2ZjYyODk2ZGQzYTMzNTE4NTEwODQ0NDRiMGRmNjA4ZGI1OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxNDRiOGRjOTYyMDg3MWM5OWJmZDU0Njg2ODk5ZDM4OTNmNmUzY2NlIn0=', '2020-01-30 23:24:41.037965'),
('wwz2bh67nsnjc7mubbtynawmwp0gtwfn', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-07 17:36:22.290694'),
('wznyfs28k1xc1jhzu3upmjtmgmh6vdn7', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-23 01:49:59.967191'),
('x771i6x6pb5fbp3u1yw62mdwbpk91l9g', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2021-01-06 17:08:06.193348'),
('xdvrplyww1ug9fpmlvcqbjhxqh30f26h', 'e30:1nlrmz:QxRftIaEVub1HMHley1j4UEzuP6ZwAZQWucK1KbwXi8', '2022-05-17 12:38:01.984453'),
('xh5q14lcbkaglsemh2kvu2zq385hbsex', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-28 01:57:19.793982'),
('xi7izxkp5h80pvgithufie37f3j16kr7', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-09 12:47:21.827673'),
('xqpw5baq35djy0imqdglavmklkn0vob5', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:25:52.132842'),
('xwjuzionqx08knntcq8pbd6przcnpon8', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-11-30 01:39:09.198816'),
('ytcml4fr664p2inftcr4ogyqg8w8ivjg', 'YTFhMzM2ZjYyODk2ZGQzYTMzNTE4NTEwODQ0NDRiMGRmNjA4ZGI1OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxNDRiOGRjOTYyMDg3MWM5OWJmZDU0Njg2ODk5ZDM4OTNmNmUzY2NlIn0=', '2020-03-14 17:54:13.363875'),
('yxo6st4kxo1fc42k4y0n2h1s1rnifwg4', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:26:46.158170'),
('z4ymozmb63dfs9cj6s9lm50i76yozxup', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:25:18.026201'),
('zceump9npkjqcvof59zhvoo5if0y7jj5', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2021-01-13 16:14:33.381887'),
('zial4koemeby2nwkaddauxricnjy78u6', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-08 20:25:57.162229'),
('zq6bzjo2aso7vgcnl92t79udg0eie3ji', 'YTFhMzM2ZjYyODk2ZGQzYTMzNTE4NTEwODQ0NDRiMGRmNjA4ZGI1OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxNDRiOGRjOTYyMDg3MWM5OWJmZDU0Njg2ODk5ZDM4OTNmNmUzY2NlIn0=', '2020-05-15 21:50:00.493519'),
('zynr9caxvixr0pbvm2pqq901oo92t1vj', 'NzgyODBkZmY3MTMzOWE1ODEwNjA1YzYxY2NlYjkxNjgzZDNmNjkxMjp7fQ==', '2020-12-30 18:24:49.440649');

-- --------------------------------------------------------

--
-- Table structure for table `events`
--

CREATE TABLE IF NOT EXISTS `events` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `city` varchar(255) NOT NULL,
  `location` varchar(63) NOT NULL,
  `show_map` tinyint(1) NOT NULL,
  `start` datetime(6) NOT NULL,
  `end` datetime(6) DEFAULT NULL,
  `public` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `events`
--

INSERT INTO `events` (`id`, `name`, `description`, `address`, `city`, `location`, `show_map`, `start`, `end`, `public`) VALUES
(1, 'Digital Prayer at Speculum Atrium', '<p>Kristina Tica&#39;s Digital Prayer will be one of the exhibits featured on this year&#39;s Speculum Atrium. Remember Digital Prayer project? Ortodox Christian icons generated using machine learning?&nbsp;Yeah, that&#39;s it. I did programming and general coding assistance which makes me proud.&nbsp;</p>', NULL, 'Trbovlje', '46.1503156,15.0443189', 1, '2020-10-15 16:00:00.000000', '2020-10-17 16:00:00.000000', 0);

-- --------------------------------------------------------

--
-- Table structure for table `images`
--

CREATE TABLE IF NOT EXISTS `images` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `images`
--

INSERT INTO `images` (`id`, `name`, `file`) VALUES
(1, 'shushko priest', 'IMG_20191109_131406_LvlNqrd.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `news`
--

CREATE TABLE IF NOT EXISTS `news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `text` longtext NOT NULL,
  `public` tinyint(1) NOT NULL,
  `language` varchar(3) NOT NULL,
  `image` varchar(100) NOT NULL,
  `date_published` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `news`
--

INSERT INTO `news` (`id`, `title`, `text`, `public`, `language`, `image`, `date_published`) VALUES
(1, 'There is no place I would rather be', '<p>Hi again, different day, different media, it&#39;s only me that is&nbsp;getting older. I hope this here to be my promised land to try out some things,&nbsp;blog is only the beginning and I wouldn&#39;t bother much doing it if it does not serve as a basis&nbsp;for something larger. It will not be spoekn about yet, but as it takes shape slowly it will crawl out on these pages. For now you will have news, blog posts, some info on my music and poetry, and I will make regularly new content as well as improve the form of it. It will not be always in English, or it will not nescessarily be in any language at all.</p>\r\n\r\n<p>And in the end you should say something like &quot;I knew it, I knew all along, no other Mali Robot could take his place&quot;. Because it&#39;s not about Ex&gt;Misha anymore, not about Celik Promet, but about qualitative sum of things which for now could just seem like some seisse verbosity without actual need for that.</p>\r\n\r\n<p>And it will gradually get self-justified&nbsp;if not evident immediatelly through the spectacle before the eyes (ears), enclosing it&#39;s own space where it draws the line to the outside though engaging as if it is and always been outside.</p>\r\n\r\n<p>Also, it should be funny in a way.&nbsp;&nbsp;&nbsp;&nbsp;</p>', 1, 'eng', 'static/images/Ray_Anthony_New_York_N.Y._ca._Aug._1947_William_P._Gottlieb_00121_ZcS2Vbz.jpg', '2019-08-05 20:44:06.000000'),
(2, 'Let\'s put the fun back in autochauvinism', '<p>And if police is so corrupted and intertwined with criminals, becoming undistiguishible from one that it should fight against, then it&#39;s all fine, since in that case it is always at the scene of the crime.&nbsp;</p>\r\n\r\n<p>--------------</p>\r\n\r\n<p>I am making far less progress on my nonlinear blog and far more music, but that&#39;s how it is for now. I do code a lot other things and I will get back eventually to this.</p>', 1, 'eng', '', '2019-08-19 20:45:58.000000'),
(3, 'Allow me to care', '<p>I did some silly bunch of songs, 20 something of them, using my relatively new equipmet and I&#39;m having a blast so far working on them.&nbsp;Of great&nbsp;help was a borrowed bass guitar and again it shows that that instrument is helping me be more productive, as it&#39;s always easier to come up with some melody using bass. This bunch of songs will eventually turn into something, an album I guess, and it will be the most energetic and compact release in years for me.&nbsp;</p>\r\n\r\n<p>In the other news I got hurt by following sports, I got angry on left, center and right, and miserble as I try to achieve things that are constantly out of my reach.&nbsp;</p>\r\n\r\n<p>But on the bright side some good thing happened after a lot of work, my assistance to Kristina&nbsp;Tica on her work for an excellent and very itneresting festival <a href=\"https://muzejnt.rs/sutra\">S.U.T.R.A.</a>&nbsp;called <strong>VI ikone</strong> has proven to be a success. I consider it a success in several ways. For one, it&#39;s my first public work in computing since I started doing it that has something to do with art, excelly which is art <em>per se.&nbsp;</em>Second, I finally got to work with GAN alghorythm whch I never did before. And finally, I discovered how to use Google Cloud in a smart way so my computer does not have to sweat it to produce something which requires long time to be rendered, which saved us much time and nerves.&nbsp;</p>\r\n\r\n<p>That&#39;s it for this news. I might write some blog entry soon, and gradually I should shift more focus to my Nonlinear app very soon, so it becomes something real nto just a plaything in my mind.</p>', 1, 'eng', 'static/images/crux_vRrdaG7.png', '2019-09-15 20:47:59.000000'),
(4, 'Civilization II', '<p>There used to be a nice post about a game called Civilization and this thing called patience. Now it&#39;s not here anymore. This is a new post till I try to recover my great piece from oblivion. Therefore this post will be called Civilization II till we find the original, or I manage to write Civlization III, or even better, IV.</p>', 1, 'eng', 'static/images/6s3g191cp0r11-ConvertImage_qs6oqVg.jpg', '2019-11-17 22:54:57.000000'),
(6, 'Unreleasing releases', '<p>I think this should be a new thing: unreleasing albums. Be brave, face it, sometimes it&#39;s better to drown it in the past. But, event like that&nbsp;coud also gather some positive attention and hype. Some fans typically dislike some albums, and in cases when band didn&#39;t have any decent release&nbsp;in years, it could be used to draw a line: on this side is a good productive past, on the right, less than great more recent past or sad present time. And I think the authors would have right, morally and legally and in whatever other way to disown the releases.&nbsp;&nbsp;</p>\r\n\r\n<p>Think of this scenario. The band is multiplatinum or whatever&nbsp;album seller, and they suddenly decide, &quot;this release is subpar, what we were thinking&quot; (think of Cut the Crap by The Clash if it makes it easier). &quot;Let&#39;s edit the memory of our band so that we become better, more flawless if not completely flawless band&quot;. And if you are true fun you will follow. Others may disobey or even laugh at the idea, but they could be minority. In time, the album may be considered some demo collection, almost a bootleg, without official stamp.&nbsp;</p>\r\n\r\n<p>There are many bad albums in this world, some of whcih should have never seen the light ot the day. Think of the future, rerelases! All the plastics, we could help the planet as well.&nbsp;</p>\r\n\r\n<p>Unreleasing album could be the news. Imagine countdown, the wait, and when the time comes, a big banner would come up saying - band&#39;s history just got better!</p>', 1, 'eng', 'static/images/photo-full.jpg', '2019-11-24 00:53:03.000000'),
(7, 'Steve Jones', '<p>There&#39;s a Sex Pistol for every age, but don&#39;t get me wrong. When I was a teenager my favorite band member was naturally Sid Vicious. Because it&#39;s important for a teenager to be seen, to look cool, and some violence on both receiving and giving end was kind of romantic. Then you grow up a little, you figure it&#39;s also important to be smart, but also still kind of cool looking but more in eccentric way. Talking about unversity years, and even some years before that, Jonny Rotten was my favorite Pistol. I mean nothing beats good provocation and supreme rightous arrogance. You grow up still and come to like Malcolm McLaren as grand master of eveything. Proven artist with theory behind him. Not a great looker, but it&#39;s not at all about looks, it&#39;s just brains. Than you start getting tired in your forties, now it&#39;s Steve Jones time, it&#39;s having fun, or what&#39;s left of it, in a lusty way, because tomorrow is maybe never. And then hopefully you become so old that Paul Cook becomes your favorite, because, I don&#39;t know, being tidy and normal? I know for sure Glen Matlock won&#39;t make it to become the favorite one and I just know it.</p>', 1, 'eng', 'static/images/1484331809-steve-jones_bhHU13Y.jpg', '2020-01-09 21:50:45.000000'),
(8, 'This was a reserved post', '<p>This was a reserved post meant for the 8th of March. How quickly time passes, from this perspective it seems so distant, things like Women&#39;s Day belong to distant past, safe past which is not aware of our troubles. It just does not care as it is not aware yet as it exists in world where death does not exist.&nbsp;</p>\r\n\r\n<p>But enough stating the obvious. What is not obvious? Is it this - stuck in apartment doing nothing next 3,4,.. 8 months? Nobody knows. All this time to be creative and yet opstipation is all you find. As if you are emergency, all anxious, and don&#39;t want to be cought by your enemy with pants down. Shit no more! Always move, especially in your mind, to the other places. Even this date is not real. 8th of March? No,&nbsp;it&#39;s April, not the 1st but a bit later.&nbsp;</p>\r\n\r\n<p>Little have I known that every band would soon be house band. Concept I was so delighted with in the past. Now we are all portable but with nowhere to go. Drinking IPA beer from middle class home and waiting till it&#39;s over. And then when the second wave comes, do it all over again, and the same after the third wave, and so on. Taking a cat outside on a leash, in prescribed hours when it&#39;s permitted. And working from home. Some things never change.&nbsp;</p>\r\n\r\n<p>I will be yelling to my microphone I lot I guess these days, and finish up this bunch of songs I started in August last year thinking I would be finished in a month or two. At least that&#39;s what I should do, but I study exponential function graphs too much.&nbsp;</p>', 1, 'eng', 'static/images/1_ggR4weAGmre9DB3Har3zbQ.png', '2020-03-08 22:17:28.000000'),
(9, 'Happy May Day, mayday, we are going down', '<p>Another retroactively published post. MayDay it is. May Day it was.&nbsp;</p>\r\n\r\n<p>I posted some lyrics, I mean poems that are actually lyrics for my next album. So now you know I haven&#39;t given up on my new album, I haven&#39;t even given up on this website as you can see. Back to the poems, silly me, I wasn&#39;t aware about encoding issues so now you have garbled text which you will see if you visit website now. But it&#39;s funny, because by the time you read this post that issue will be fixed. I wanted to post more stuff but somehow my other poems got lost in the cloud. I guess the cloud rained down, and now I need to check my computers because my poems are scattered all over the place!</p>\r\n\r\n<p>Focusing on work does help to deal with this a situation, which still feels like a timeless limbo on endless repeat. The real issue is that my life is completely the same, except that I still work, and yes I have work and I can work&nbsp;from home which somehow isn&#39;t consoling at all, and I, like many others, wonder about everything... Not the perfect creative&nbsp;atmosphere mind you. But new songs are my focus, and my focus is unofocused, and it&#39;s like a radio station from a far away, so sometimes you get a good signal, sometimes you don&#39;t. But ultimately, nobody&#39;s expecting creative&nbsp;burst from anyone, let alone myself, so I am just a drama queen, my own evil master, but still a master, huh.&nbsp;&nbsp;</p>', 1, 'eng', 'static/images/f24728b492ee359a865221482337bff1.gif', '2020-04-30 22:50:11.000000'),
(10, 'Out of the quarantine, into the void', '<p>When out of the quarantine only to find that quarantine is a multilayered thing, it does applies to staying at home only, as you go out you will find many other not so obvious limits. But they are there, it&#39;s not only limits imposed by the situation, but also ones that are internal, self imposed. Therefore, the world is still a bit lifeless, colorless, call it like you want. It&#39;s a great looking cookie, but it has no taste at all. You can watch it, but you cannot enjoy it. Thus, I would rather go back inside then see the outside in this sorry state. Alas, not everybody agrees, but I just can&#39;t get into that mindset.&nbsp;</p>\r\n\r\n<p>And at home, I have create void. Hopefully that will end up soon. Just had too much frustration with writing lyrics for my song. I am hardly satisfied with lyrics I&#39;ve written so far, but I am even less satisfied with vocal tracks for my new album. But I guess dissatisfaction is a part of the process. I would pretend that I am in no hurry, although I am very much because I want this done so I can move to new adventures, and I don&#39;t want to see anything unfishied, especially if I think it is good overall, otherwise I wouldn&#39;t bother.&nbsp;</p>\r\n\r\n<p>&nbsp;</p>', 1, 'eng', 'static/images/Black-is-solid-and-white-is-void-space-a-Pore-space-between-grains-b-pore-space-as.png', '2020-05-13 21:15:51.000000'),
(11, 'Tour de Misha', '<p>Oh my dear friends, it&#39;s been a while! That doesn&#39;t mean I wasn&#39;t doing anything. Quite the opposite, making the album took a lot of time and work was hard, still I am close to finishing it. There were few Digital Prayer exibitions in the meantime, and when I could I did small incremental updates to this site but had very little time to put in any content. I hope this is going to change, but I have many plans in the pipeline so I could easily get overwhelmed again, need to be careful there!&nbsp;</p>\r\n\r\n<p>At least in these Corona times, staying and home and working on things seems like an only option for some fun. I should also revamp Ex&gt;Misha site, but just thinking about&nbsp;going through it again scares me a bit. I will try to start small and gradually build it, if I ever start that is.&nbsp;</p>\r\n\r\n<p>Obviously no concert reviews or real life stories to write about, and I try to stay away from venting political anger because it is futile anyway. We do that on social networks anyway.&nbsp;Instead,&nbsp;let&#39;s do something constructive. But hey in this hypnotically boring lockdown life I can only think of writing about how I like to play Train Simulator or take my cat out on a leash. One other thing I am likely to write is to explain my lo-fi style why I stick to it in music and where I think it will get me. All in due time.</p>\r\n\r\n<p>Album has to be finished this week, and then I have to wait for cover art which hopefully I am not going to do myself this time. Outsourcing is a great option now when the time is tight. A month ago I thought that was it, then I went on remixing spree. Last week a great new idea came up for a song. I loved it so much that I am postponing a release just finish it and include on the album.&nbsp;That&#39;s it for now, hope I will get back to writing before I get overwhelmed with other ideas.</p>', 1, 'eng', 'static/images/960x0.png', '2020-11-23 21:48:06.000000');

-- --------------------------------------------------------

--
-- Table structure for table `poems`
--

CREATE TABLE IF NOT EXISTS `poems` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `text` longtext NOT NULL,
  `public` tinyint(1) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `poems_author_id_9cbe9b0c_fk_auth_user_id` (`author_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `poems`
--

INSERT INTO `poems` (`id`, `title`, `text`, `public`, `date_created`, `author_id`) VALUES
(1, 'Kako sam rekao', 'A šta sam rekao', 1, '2020-01-16 23:28:00.000000', 1),
(3, 'Tehnika', '<p>&nbsp;</p>\r\n\r\n<p>Jo&scaron; sam bolji a tek sam počeo</p>\r\n\r\n<p>Tehnika, Tehnika</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>Od svake slabosti ne&scaron;to se nauči</p>\r\n\r\n<p>Tehnika, Tehnika</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>Bolji uvek sme da se ljuti</p>\r\n\r\n<p>Tehnika, Tehnika</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>Nosi se sa tim&nbsp;&nbsp;</p>\r\n\r\n<p>Ako ima&scaron; ima&scaron; dobre volje</p>\r\n\r\n<p>Život sa njim</p>\r\n\r\n<p>Pažnje iziskuje preko volje</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>On će da ponovi</p>\r\n\r\n<p>Pa ponovi</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>To će da se ponovi</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>Ne talasa, ide na put</p>\r\n\r\n<p>Nema torbu, ima zanat</p>\r\n\r\n<p>Biće to dobar rat</p>\r\n\r\n<p>Živeo, živeo rat</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>Hiljadu cvetova</p>\r\n\r\n<p>Dođe i nestane</p>\r\n\r\n<p>Ja ne želim da prestane</p>\r\n\r\n<p>Ne zaboravi me</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp;</p>', 1, '2020-05-01 21:50:15.000000', 1),
(4, 'Kičma', '<p>Zabada&scaron; i odigrava&scaron; vreme</p>\r\n\r\n<p>Ni&scaron;ta se nije jo&scaron; dogodilo</p>\r\n\r\n<p>Samo ono &scaron;to je moglo</p>\r\n\r\n<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>\r\n\r\n<p>Sada&scaron;njost je otpad pro&scaron;losti</p>\r\n\r\n<p>Đubre moje duboko</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>Sistem je preterano dobar</p>\r\n\r\n<p>Mnogo se baca sa strane</p>\r\n\r\n<p>Svuda su o&scaron;tre ivice</p>\r\n\r\n<p>Ranjeni su prsti budale</p>\r\n\r\n<p><br />\r\n&nbsp;</p>\r\n\r\n<p>Dođi opet, al&rsquo; dođi juče</p>\r\n\r\n<p>Nedostaje&scaron;</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>Probaj opet, dok nisam tu</p>\r\n\r\n<p>Zakasniće&scaron;</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>Verujem da postoji&nbsp;</p>\r\n\r\n<p>Sirovost izvanredna</p>\r\n\r\n<p>Slepa paljba i&nbsp;</p>\r\n\r\n<p>Benedikcija</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>Mnoge &scaron;anse su previ&scaron;e &scaron;ansi</p>\r\n\r\n<p>Navika je postala jaka</p>\r\n\r\n<p>Glava je beskonačna</p>\r\n\r\n<p>Kičma može biti jaka</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>Mali Njutn&nbsp;</p>\r\n\r\n<p>Mora moći</p>\r\n\r\n<p>Potisak</p>\r\n\r\n<p>Uzdiže</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>&nbsp;</p>', 1, '2020-05-01 21:52:46.000000', 1);

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE IF NOT EXISTS `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `lead` varchar(255) NOT NULL,
  `text` longtext NOT NULL,
  `public` tinyint(1) NOT NULL,
  `language` varchar(3) NOT NULL,
  `image` varchar(100) NOT NULL,
  `date_published` datetime(6) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `posts_author_id_099b8aca_fk_auth_user_id` (`author_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`id`, `title`, `lead`, `text`, `public`, `language`, `image`, `date_published`, `author_id`) VALUES
(1, 'Review: what is not seen cannot be seen even on Youtube - postcard from Pripizdinsk oblast express', 'I was the absent audience member on several concerts. Not that it mattered much, because every interchange has an exit to Pripizdinsk and so I followed', '<p>Is a very good blog. Is in english - English not best always. But can understand mostly by anyone, yes. Face it and read on. Another thing problematic - has not been on concerts intending to write about. Not a problem, I did it once, I could do it again, faithfully. I can say everything I know about the concert I&#39;ve not been to, and now I know at least some. See, I wanted to start thsi blog of mine with a bang, but bang was infinitiely delayed, as well as any other creative ideas I had or still have. Not going to happen as I intended, but I will rumble in the mud as long as I have to to let out what I can.&nbsp;</p>\r\n\r\n<p>See, a year ago I started changing jobs. Not that it matters for this occasion directly. But I changed four jobs in the meantime because all of them felt inadequate for me. Yes, this job lacked good coffee machine, and this one lacked good comoany to talk about music, and this one job&nbsp;was too repetitive, not up to my taste, and that one had too much bad history, and that one had too much gossiping around about other coleagues, one even had toilet remotely&nbsp;but did not allow for remote work. In the end, after my final attempt to satisfy my thirst for knoledge and self improvement I landed in Pripizdinsk oblast only to find out much of the stuff I already had in my previous jobs. So, that&#39;s it, the problem is me. Very bad thing is that all these poritions forced me to be what I am not, the worker, which I never felt like. Things are rarely creative in life, that&#39;s only left to&nbsp;bourgeoisie with too much time time on their hands. When you need to take express to Pripizdinsk you know that you are not one of them. You are true to life, confined to real life conditions human vessel for pain, nausiences and boredom.&nbsp;</p>\r\n\r\n<p>Why was that important to say right now? Well, I had someone close die recently, I had to go to the funeral from my workplace and then back. Remote graveyard had strong winds blow and I got some nasty cold, feeling pretty much like zombie for the rest of the week, Exhausted mentally and phisically.&nbsp;</p>\r\n\r\n<p>Friday came and I was optimistic to come on either if not both concerts. Oh, which two concerts you ask. Of course, I failed to mention. First one is Klotljudi and Nike Eyes in Klot club, a new place which has tons of events in order to get to the map as soon as possible, and I think it already did. Second one is Yva and the Toy George, one girl band from Rome, which I already seen a couple of times, but somehow recently, and particularly since it changed her style a bit, I couldn&#39;t make to her shows here, which are too few&nbsp;anyway. So, when I learned there will be these two concerts on the same night, I was both excited and worried. Little I have known that I will not make to either of them.&nbsp;</p>\r\n\r\n<p>Come Friday I wash finishing some work which could take me as far as ... I cannot tell, let it remain secret, but there was something demanding I had to work and to which I focused all my energy. Deadline was a midnight of the very same day. I hoped I could finish to see Klotljudi first. Because who wouldn&#39;t. They are as close to The Fall, beside Klopka za pionira, that ever existed in Serbia (not counting Celik Promet here, I think they are too far to fit into &quot;The Fall like&quot; criteria). I like the singer, he has attitude, the music is loose, but rocking, and I don&#39;t know, unlike many other young bands here they do not put all their cards into pure energy (similar like during the &#39;90&#39;s it was all about funk, rhythm, reggae at the same time almost for some). Anyhow, wouldn&#39;t that be a good beginning of the night. But during their concert I was walking my cat on a lead. OK, maybe I should I have prepared you for this, maybe it&#39;s too much information, but fact is I have a cat, he want&#39;s too walk around and see stuff, but I live in a building, I cannot just let him out like that, therefore I use the lead. If I don&#39;t do it he does nasty things. It deserves story of it&#39;s own. Still I had a time to make it around 11 pm, but I was losing too much time. Oh, I had no bath! Damn, what we gonna do about this. But I feel so sick I like just lying down in my bad and watch random stuff over the internets! As if Nike Eyes hadn&#39;t took over already with their electronic grooves. I don&#39;t know yet what to make of them, even after seeing them live. Girl sings and guy plays music using machines. Sounds familiar? But it does not say a lot of music still. I found them bit on a dancing side and kind of claustrophobic in a good way I guess.&nbsp;</p>\r\n\r\n<p>I sent SMS to my friend for whom I assumed was in Kvaka 22 where Yva and the Toy George is going to play. I needed an encouragement, I needed an information. My plan was too quickly get my self ready and jump in when the concert starts and leave home after it ends. However, the answer never came, but I learned from him tomorrow that concert was excellent. I remember Yva from earlier versions, and it was still hard to pinpoint with less than a full sencence. Electro-clash, no, yes? Retro, a bit. Dancing, maybe. Somewhat ironic, check. Arty, check. However, lately it joined the wagon of music artists taking inspiration from folk music, turbo-folk if you will, and generally music phenomenon tied to a lesser culture ot the uneducated classes. With leftists the idea went upside down where now you should now feel guilty for not endorsing it. Sure I like some oriental melodies, I am little bit fed up with rock, pop music or whatever it is, I need something new. But I do not wear my taste like some kind of achievement badge. Like, &quot;hey, I am listener without prejudices level 21&quot;!&nbsp; Anyway, this has not so much to do with Yva, it is not her defining moment, as there is a lot of fun mixing of all stuff around the globe done and executed in a punkish way which I like a lot. Rather masterfully, as in song Rat (see references in the end of the text) where there is obvious global political message. But can I say more in a review of a concert I haven&#39;t been to. No, I can&#39;t. (Knope we can!).&nbsp;</p>\r\n\r\n<p>Actually since I was so&nbsp;polite to my body that I&nbsp;remained at home, it&#39;s hard to explain myself what do I want, why do I write, what does these words carry?</p>\r\n\r\n<p>A: It carries what you have to say, you are writing it to let it out, no one is going to read it anyway.</p>\r\n\r\n<p>B: It is important because everybody should know you, you are so witty writer, a word meister... I am not. I actively sabotage myself, because:</p>\r\n\r\n<p>&nbsp; &nbsp; B1: I want to be funny.</p>\r\n\r\n<p>&nbsp; &nbsp; B2: Ego attack. I think I have super powers</p>\r\n\r\n<p>C: I need a reason to finish this website in order to do other stuff with it. So many experiments await! So many tries to be tried.&nbsp;</p>\r\n\r\n<p>This is true:</p>\r\n\r\n<p>So many failures to try. Failure is a collision and it brings us closer to what&#39;s real. What is real? I am not a workhorse is one thing. I piss on it in rainbow colors.&nbsp;</p>\r\n\r\n<p>PS Apologies to all artists mentioned for my inability to say a little more. It can only get better.&nbsp;</p>\r\n\r\n<p>References:</p>\r\n\r\n<p><a href=\"https://www.youtube.com/watch?v=MOlcMUnFFBM\">https://www.youtube.com/watch?v=MOlcMUnFFBM</a></p>\r\n\r\n<p><a href=\"https://www.youtube.com/watch?v=x7weo8f1bHM\">https://www.youtube.com/watch?v=x7weo8f1bHM</a></p>\r\n\r\n<p><a href=\"https://www.youtube.com/watch?v=f5qAFk4gWMc\">https://www.youtube.com/watch?v=f5qAFk4gWMc</a></p>\r\n\r\n<p><a href=\"https://www.youtube.com/watch?v=yNHkBWAs4So\">https://www.youtube.com/watch?v=yNHkBWAs4So</a></p>', 1, 'eng', 'static/images/IMG_20191109_131406.jpg', '2019-11-17 21:51:44.000000', 1),
(2, 'Review: One they bands in my neighborhood', 'That is a singular they, to be sure. But they run in plural as well and I try to write about it in a systematic and boring way', '<p>Hello again after a long break. If you remember the previous time, you get the idea of what I am trying to do here, even if I am maybe not&nbsp;fully aware myself yet and still solitary in this mission (but I am looking to change that). Still,&nbsp;I am not the only one solitary here&nbsp;if that&rsquo;s any comfort, because so are many bands, namely, one man bands, people doing it on their own.&nbsp;OK, &ldquo;doing it on their own&rdquo; could be misleading. Nobody does all on their own because it is too much,&nbsp; so either at least someone else has to produce music, and&nbsp;someone else can direct&nbsp;a video, so&nbsp;it&rsquo;s not likely that a single person has so many talents. But on the stage they are alone, there is no rhythm section to fall back to, no keyboardist or guitarist to cover up&nbsp;when shit happens, just a mercialles automated sounds which are coming whether you like it or not. They certainly won&rsquo;t be waiting for you if you miss your part or get lost in the song.&nbsp;</p>\r\n\r\n<p>I admit, I was one of them one man bands. You see, my name was Ex&gt;Misha if you don&rsquo;t know me by now. I went so far that I even organized a festival of ona man bands (though some notably had two members but were still considered as&nbsp;single person entity). Pardon me for this long introduction, or diversion you may call it, it so much easier to speak about yourself than about the others so I am just relieving some anxiety here. Of course, I am a mess, so I do tend to fool around.&nbsp;&nbsp;</p>\r\n\r\n<p>Back when I was way more active (read: till 2015) I used to do some shows with Ivica, that&rsquo;s how I&nbsp; got to know him. In the crazy old days Ivica went from acoustic to electric sound, and performed with or without additional synth or electric guitar. Development of Ivica was an interesting thing to follow as it was not linear, and this is nonlinear blog so I am obliged to write about it. Some people define their sound and stick to it, not Ivica. But it&#39;s wrong to say&nbsp;that he&nbsp;is without continuity, as throughout his carrer his songs usually&nbsp;were mellow and intimate, with short and simple, direct lyrics, frequently in the form of addressing somebody, and singing on the edge of whispering, to put it simply - intimate. But I am sure you cannot easily frame&nbsp;Ivica, as he is constantly evolving even if sensibility stays the same. The new album, <a href=\"https://ivica.bandcamp.com/album/1235\">1235</a> sounds a bit more heavily produced&nbsp;and heading towards more electronic sound which is an interesting development.&nbsp;</p>\r\n\r\n<p>Let me take a break and say that both concerts I am going to write about took place in Knap club. Tidy and small place, but if I have to be ironic, it is a perfect fit for such a small and fragmented scene without center. I am not missing the center, but we are here and there on our own.&nbsp;</p>\r\n\r\n<p>Thus, the club was not that crowded, and seems like having a publisher, videos and media appearance do not guarantee that people would come. And this was Ivica&rsquo;s first concert in Belgrade after the album was released as a headliner, actually one and only act for the night.&nbsp;</p>\r\n\r\n<p>When the concert started I wasn&rsquo;t actually able to tell as long instrumental followed. I think I was a tiny bit late but Ivica certainly still wasn&rsquo;t on the stage, but music went on. But what followed showed than Ivica that live sound can cope with newly found complexity as now his sound is more layered I would say. It has a bunch of sounds, and it&rsquo;s all reverby, has delay effects too, and is all wrapped up like some dreamy soundscape, almost ambiental. However, lyrics are sometimes too quiet to be heard, but that&rsquo;s not a big issue, you can feel the vibe before you understand it, but throughout the show there was no significant change in dynamics even when old songs were played. However, this newly built sound opens new perspectives, and you can see how mesmerized and taken by it is Ivica when he performs.&nbsp;</p>\r\n\r\n<p>As if he is a galley navigating the ocean, with guitar lika a ship bos managing the waves, going up and down, swinging. The ocean if I am not mistaken is frequent theme in Ivica&#39;s poetry, I am trying to make sense of it but I would have to sit down and be calm individual. Having a focus is not my thing, I just rush through everything. But I know it&#39;s persistent theme, and there is a longer story there my dear Watson. But i beleive we are not talking about shipwrecking ocean, but more like something as a state of being something, something relatively stable, immersing, that swallows, but may be both a sanctuary and a trap. I am not sure and I am drinking at that moment, a let my brain wonder for a change. A let my self wonder after it, on the street, and then at home, with some more Kozel.&nbsp;</p>\r\n\r\n<p>This weekend another concert took place at the Knap, two one man bands/one woman bands, or one man band and one woman band. Playing with words is not funny. I am not trying to be funny, I just want to be correct. Anyway, welcome from Croatia - &Scaron;ećeЯ and VO&Lambda;DO!&nbsp;</p>\r\n\r\n<p>It is a good opportunity to compare these acts together, as in how many possibilities one person band offers. &Scaron;ećeЯ is Tena Rak, former drummer of Vlast Popić, legendary three piece, playing energetic and raw music but not without a sense for good melody. Did I get it right? I am not sure, the definition is too generic. How many energetic and raw three member bands are there? Exactly. But &Scaron;ećeЯ is a departure from that sound going into more electronic pop territory. There are samples, guitar, loops, vocal harmonies. VO&Lambda;DO, on the other hand, is more &ldquo;live&rdquo;, in the sense that he creates his sounds using looper right there on the stage, making his beat and melody, gradually adding more details to the song, so we can witness it being compiled and put together.&nbsp;</p>\r\n\r\n<p>I was surprised to see how empty the club was even when the concert started. Of those who came, many of them were members of the scene, friends of the bends, likely from tours or whatever. So it&rsquo;s even harder for Croatian bands to fill up the club then it is for homegrown ones. Maybe sudden weather changes made them feel tired so they stayed home. Who knows, not me, I never lost Saturday night!</p>\r\n\r\n<p>Standing on the verges of a very wide half circle that audience formed around the stage, with r = 3m, I was too shy to go forward. Man, this intimacy is stinging me. But what I saw was similar to a street musician performance. VO&Lambda;DO seems to be skilled in what he does. We learned from him that he started playing solo one month ago. Member of From Another Mother, a frantic and energetic band, what he does solo is a way more tame. Indie folk or what you may call it, nonetheless, it sounds like something right from the USA, and it&rsquo;s sung in English. Maybe too sweet for my taste, but commercial potential is there, you can sing along to choruses and stuff. What he plays stills sounds full and reach, he certainly won&rsquo;t complain about the lack of people with him in the band! Like I said, he is skillful but in a way that street musicians are when they fascinate with some tricks, but unlike them this guy has his own songs. And he sounds organic as the all sounds he creates I think come just from his tiny little guitar and a pedal (which makes his appearance even more remarkable).&nbsp;</p>\r\n\r\n<p>Best movie role for&nbsp;VO&Lambda;DO? Street musician on the streets of Barcelone. It&#39;s always sunny, everybody loves him, then there&#39;s a twist, a break in harmony, but still happy end awaits, and love remains triumphant. The music ma be too american for that kind of movie, but we can imagine differently.&nbsp;</p>\r\n\r\n<p>Next we had a lengthy pause in order for some particular people to come to the concert. I know because we were told by &Scaron;ećeЯ. No, I don&rsquo;t know which people. But we&rsquo;ve been briefed in the meantime by some girl from a certain organisation about February 29th, that is, Rare Disease Day, because it&rsquo;s every four years, you get that.&nbsp;</p>\r\n\r\n<p>Damn the day when I decided this is going to be a single review. I already wrote too much and still have to write. Do you know that it&rsquo;s harder for me to shorten existing text than to write shorter text from the beginning? But time is critical and I have only one go at this.</p>\r\n\r\n<p>To be honest I haven&rsquo;t been following much of what is going on with &Scaron;ećeЯ. I would hear that there is a gig here and there in Belgrade but never went to any. Looking for things to see over the weekend I played a few tunes to convince me to go.&nbsp;</p>\r\n\r\n<p>Music is a bit minimal, and certainly is better suited for smaller crowds. I like the interplay of simple beats and keyboard melodies, sampled guitar cutouts, and echoed vocals. It&rsquo;s all cleverly put together, gradually kicking in till it resolves in a spectacular way. Mood is something between mellow and melodic to the kind of darker and more psychedelic tunes (in a PJ Harvey way? No, that could be a misleading reference). Minimalist approach here is somehow inviting to the listener, it does not grab you immediately but instead it keeps distance and lets you gradually be absorbed by it. As a performer Tena is very relaxed, and frequently gets off the stage to join the audience. Much of the performance is hands free, so she can concentrate on singing which is another great quality. The set didn&rsquo;t last long as she only has one full release and several singles, but the songs themselves are not long too.&nbsp;</p>\r\n\r\n<p>Full of impressions I hit the streets, buying 150g Smoki at the kiosk. It&rsquo;s still a weekend. But before that I expected to see a vintage american car which was parked near the Knap the previous Saturday. I couldn&rsquo;t find it this time. I wanted to take a proper photo of it this time.&nbsp;</p>\r\n\r\n<p>References:</p>\r\n\r\n<p><a href=\"https://ivica.bandcamp.com/\">https://ivica.bandcamp.com/</a></p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p><iframe frameborder=\"0\" height=\"315\" src=\"https://www.youtube.com/embed/VchZVU9x5oE\" width=\"560\"></iframe><iframe frameborder=\"0\" height=\"315\" src=\"https://www.youtube.com/embed/Gd47dQNvoI4\" width=\"560\"></iframe><iframe frameborder=\"0\" height=\"315\" src=\"https://www.youtube.com/embed/WkDpX08o9Ec\" width=\"560\"></iframe></p>', 1, 'eng', 'static/images/IMG_20200301_000543.jpg', '2020-03-01 12:44:53.000000', 1);

-- --------------------------------------------------------

--
-- Table structure for table `taggit_tag`
--

CREATE TABLE IF NOT EXISTS `taggit_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `slug` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `taggit_tag`
--

INSERT INTO `taggit_tag` (`id`, `name`, `slug`) VALUES
(1, 'Ivica', 'ivica'),
(2, 'Secer', 'secer'),
(3, 'concert', 'concert'),
(4, 'Voado', 'voado');

-- --------------------------------------------------------

--
-- Table structure for table `taggit_taggeditem`
--

CREATE TABLE IF NOT EXISTS `taggit_taggeditem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_id` int(11) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `taggit_taggeditem_content_type_id_object_id_tag_id_4bb97a8e_uniq` (`content_type_id`,`object_id`,`tag_id`),
  KEY `taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id` (`tag_id`),
  KEY `taggit_taggeditem_object_id_e2d7d1df` (`object_id`),
  KEY `taggit_taggeditem_content_type_id_object_id_196cc965_idx` (`content_type_id`,`object_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `taggit_taggeditem`
--

INSERT INTO `taggit_taggeditem` (`id`, `object_id`, `content_type_id`, `tag_id`) VALUES
(5, 2, 7, 1),
(6, 2, 7, 2),
(7, 2, 7, 3),
(8, 2, 7, 4);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `albums`
--
ALTER TABLE `albums`
  ADD CONSTRAINT `albums_image_id_5e8a0206_fk_images_id` FOREIGN KEY (`image_id`) REFERENCES `images` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `comments_post_id_67cfce36_fk_posts_id` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `poems`
--
ALTER TABLE `poems`
  ADD CONSTRAINT `poems_author_id_9cbe9b0c_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `posts`
--
ALTER TABLE `posts`
  ADD CONSTRAINT `posts_author_id_099b8aca_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `taggit_taggeditem`
--
ALTER TABLE `taggit_taggeditem`
  ADD CONSTRAINT `taggit_taggeditem_content_type_id_9957a03c_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `taggit_tag` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
