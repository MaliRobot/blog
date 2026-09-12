import os
from pathlib import Path
from ctypes import CDLL

def load_gdal():
    """
    On Windows, ensures that the GDAL DLL directory is in the DLL search path
    and pre-loads the GDAL DLL to avoid 'WinError 127' during Django's startup.
    """
    if os.name == 'nt':
        try:
            # We use decouple if available, otherwise fallback to os.environ
            try:
                from decouple import config
                gdal_path = config('GDAL_LIBRARY_PATH', default=None)
            except ImportError:
                gdal_path = os.environ.get('GDAL_LIBRARY_PATH')

            if gdal_path and Path(gdal_path).exists():
                # Only use it if it's a Windows-style path or exists
                # In Docker/Linux, we should not be here due to os.name == 'nt'
                gdal_dir = Path(gdal_path).parent
                # Add the directory to the DLL search path (Python 3.8+)
                if hasattr(os, 'add_dll_directory'):
                    os.add_dll_directory(str(gdal_dir))
                # Pre-load the DLL to ensure all dependencies are resolved
                CDLL(gdal_path)
        except Exception:
            # Silence errors to avoid blocking startup if GDAL is not needed or missing
            pass
    elif os.environ.get('GDAL_LIBRARY_PATH'):
        # If GDAL_LIBRARY_PATH is set on non-Windows (e.g. Docker), 
        # ensure it's a valid path for the current OS.
        # If it looks like a Windows path (has C:), we should probably ignore it.
        gdal_path = os.environ.get('GDAL_LIBRARY_PATH')
        if ':/' in gdal_path or ':\\' in gdal_path:
             # Likely a Windows path passed to Linux container, unset it for this process
             os.environ.pop('GDAL_LIBRARY_PATH', None)
