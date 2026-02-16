# -*- coding: utf-8 -*-
"""
Shadow Touch Helper - Configuration Module
Manages API keys, settings, and configuration for the skin helper
"""

import xbmc
import xbmcaddon

# Get addon instance
ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_NAME = ADDON.getAddonInfo('name')

# TMDB API Configuration
# NOTE: This is a public test API key for testing purposes only
# For production, get your own free key at https://www.themoviedb.org/settings/api
# This key has rate limits and may stop working if overused!
TMDB_API_KEY = "8d6d91941230817f7807d643736e8a49"  # Public test key
TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p"

# Image sizes
TMDB_POSTER_SIZE = "w500"  # Options: w92, w154, w185, w342, w500, w780, original
TMDB_BACKDROP_SIZE = "w1280"  # Options: w300, w780, w1280, original
TMDB_PROFILE_SIZE = "w185"  # Options: w45, w185, h632, original

# Cache settings
CACHE_ENABLED = True
CACHE_DURATION = 3600  # 1 hour in seconds


def get_setting(setting_id, default=None):
    """
    Get addon setting value

    Args:
        setting_id (str): Setting ID to retrieve
        default: Default value if setting not found

    Returns:
        Setting value or default
    """
    try:
        value = ADDON.getSetting(setting_id)
        if value:
            return value
        return default
    except Exception as e:
        xbmc.log(f"[{ADDON_NAME}] Error getting setting '{setting_id}': {str(e)}", xbmc.LOGERROR)
        return default


def set_setting(setting_id, value):
    """
    Set addon setting value

    Args:
        setting_id (str): Setting ID to set
        value: Value to set

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        ADDON.setSetting(setting_id, str(value))
        return True
    except Exception as e:
        xbmc.log(f"[{ADDON_NAME}] Error setting '{setting_id}': {str(e)}", xbmc.LOGERROR)
        return False


def get_tmdb_api_key():
    """
    Get TMDB API key from settings or use default

    Returns:
        str: TMDB API key
    """
    # Try to get from our addon settings first
    api_key = get_setting('tmdb_api_key')
    if api_key:
        return api_key

    # Try to get from TMDB Helper addon (if installed)
    try:
        tmdb_helper = xbmcaddon.Addon('plugin.video.themoviedb.helper')
        api_key = tmdb_helper.getSetting('tmdb_apikey')
        if api_key:
            log_info(f"Using TMDB API key from TMDB Helper addon")
            return api_key
    except Exception as e:
        log_debug(f"Could not get API key from TMDB Helper: {str(e)}")

    # Fall back to hardcoded key
    log_error("No valid TMDB API key found! Please configure one in addon settings.")
    return TMDB_API_KEY


def log(message, level=xbmc.LOGDEBUG):
    """
    Log message with addon name prefix

    Args:
        message (str): Message to log
        level: Log level (xbmc.LOGDEBUG, xbmc.LOGINFO, xbmc.LOGWARNING, xbmc.LOGERROR)
    """
    xbmc.log(f"[{ADDON_NAME}] {message}", level)


def log_error(message):
    """Log error message"""
    log(message, xbmc.LOGERROR)


def log_info(message):
    """Log info message"""
    log(message, xbmc.LOGINFO)


def log_debug(message):
    """Log debug message"""
    log(message, xbmc.LOGDEBUG)
