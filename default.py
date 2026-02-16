# -*- coding: utf-8 -*-
"""
Shadow Touch Skin Helper
Entry point for skin helper script

This script provides TMDB API integration and action handlers
for the Shadow Touch skin, particularly for long-press overlay functionality.

Usage from skin XML:
    RunScript(skin.shadow.touch,action=show_movie_info,tmdb_id=12345)
    RunScript(skin.shadow.touch,action=show_movie_info,title=Inception,year=2010)
    RunScript(skin.shadow.touch,action=clear_movie_info)
    RunScript(skin.shadow.touch,action=add_to_watchlist,tmdb_id=12345)
    RunScript(skin.shadow.touch,action=mark_as_watched,tmdb_id=12345)

Author: Shadow Touch Team
License: GPL v2
"""

import sys
import xbmc
import xbmcaddon

# Add resources/lib to Python path
addon_path = xbmcaddon.Addon().getAddonInfo('path')
sys.path.insert(0, addon_path)

from resources.lib.modules.router import routing


if __name__ == '__main__':
    try:
        # Log script start
        xbmc.log("[Shadow Touch Helper] Script started", xbmc.LOGINFO)
        xbmc.log(f"[Shadow Touch Helper] sys.argv: {sys.argv}", xbmc.LOGDEBUG)

        # Run router
        routing()

        xbmc.log("[Shadow Touch Helper] Script finished", xbmc.LOGINFO)

    except Exception as e:
        xbmc.log(f"[Shadow Touch Helper] Fatal error: {str(e)}", xbmc.LOGERROR)
        import traceback
        xbmc.log(f"[Shadow Touch Helper] Traceback:\n{traceback.format_exc()}", xbmc.LOGERROR)
