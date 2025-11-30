# loanersys/utils.py
import os
import logging
from datetime import datetime
from .config import SHARED_PATH, LOG_FILE

def setup_shared_directory():
    """Setup shared directory with proper permissions"""
    try:
        # Create shared directory if it doesn't exist
        os.makedirs(SHARED_PATH, exist_ok=True)
        
        if os.name == 'nt':  # Windows
            import win32security
            import ntsecuritycon as con
            
            # Get everyone SID
            everyone = win32security.ConvertStringSidToSid("S-1-1-0")
            
            # Set permissions
            security = win32security.GetFileSecurity(
                SHARED_PATH, 
                win32security.DACL_SECURITY_INFORMATION
            )
            dacl = win32security.ACL()
            dacl.AddAccessAllowedAce(
                win32security.ACL_REVISION,
                con.FILE_ALL_ACCESS,
                everyone
            )
            security.SetSecurityDescriptorDacl(1, dacl, 0)
            win32security.SetFileSecurity(
                SHARED_PATH, 
                win32security.DACL_SECURITY_INFORMATION, 
                security
            )
        else:  # Linux/Mac
            os.chmod(SHARED_PATH, 0o777)  # Full permissions for all users
            
    except Exception as e:
        print(f"Error setting up shared directory: {e}")
        return False
    return True

def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Set file permissions for log file
    try:
        if os.name != 'nt':  # Linux/Mac
            os.chmod(LOG_FILE, 0o666)
    except Exception as e:
        print(f"Error setting log file permissions: {e}")

def log_action(action, user, details):
    """Log user actions"""
    logging.info(f"{action} - User: {user} - Details: {details}")
