# -*- coding: utf-8 -*-
"""
Shadow Touch Helper - Action Handlers
Handles user actions like long-press, movie info fetching, etc.
"""

import xbmc
import xbmcgui
import xbmcaddon
import requests
import json

from .config import (
    get_tmdb_api_key,
    TMDB_BASE_URL,
    TMDB_IMAGE_BASE_URL,
    TMDB_POSTER_SIZE,
    TMDB_BACKDROP_SIZE,
    log_error,
    log_info,
    log_debug,
    get_setting
)


def clear_movie_info():
    """
    Clear movie info properties
    Used to reset window properties before loading new movie data
    """
    window = xbmcgui.Window(10000)  # Home window
    properties = [
        'ShadowTouch.MovieTitle',
        'ShadowTouch.MoviePlot',
        'ShadowTouch.MovieRating',
        'ShadowTouch.MovieYear',
        'ShadowTouch.MoviePoster',
        'ShadowTouch.MovieBackdrop',
        'ShadowTouch.MovieGenres',
        'ShadowTouch.MovieRuntime',
        'ShadowTouch.MovieCast',
        'ShadowTouch.MovieDirector',
    ]

    for prop in properties:
        window.clearProperty(prop)

    log_debug("Cleared movie info properties")


def get_movie_info(tmdb_id=None, title=None, year=None):
    """
    Fetch movie information from TMDB API

    Args:
        tmdb_id (str/int): TMDB movie ID
        title (str): Movie title (used if tmdb_id not provided)
        year (str/int): Movie year (optional, for better search accuracy)

    Returns:
        dict: Movie information or None if not found
    """
    api_key = get_tmdb_api_key()

    if not api_key or api_key == "YOUR_TMDB_API_KEY_HERE":
        log_error("TMDB API key not configured!")
        xbmcgui.Dialog().notification(
            "Shadow Touch",
            "TMDB API key not configured. Please check addon settings.",
            xbmcgui.NOTIFICATION_ERROR,
            3000
        )
        return None

    try:
        # If TMDB ID provided, fetch directly
        if tmdb_id:
            url = f"{TMDB_BASE_URL}/movie/{tmdb_id}"
            params = {
                'api_key': api_key,
                'language': 'de-DE',  # German language
                'append_to_response': 'credits'  # Get cast/crew info
            }

            log_debug(f"Fetching movie info for TMDB ID: {tmdb_id}")
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()

        # Otherwise search by title
        elif title:
            url = f"{TMDB_BASE_URL}/search/movie"
            params = {
                'api_key': api_key,
                'language': 'de-DE',
                'query': title,
                'include_adult': False
            }

            if year:
                params['year'] = year

            log_debug(f"Searching movie: {title} ({year if year else 'no year'})")
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            results = response.json().get('results', [])

            if results:
                # Get detailed info for first result
                return get_movie_info(tmdb_id=results[0]['id'])
            else:
                log_error(f"No results found for: {title}")
                return None

        else:
            log_error("No TMDB ID or title provided")
            return None

    except requests.exceptions.RequestException as e:
        log_error(f"Error fetching movie info: {str(e)}")
        xbmcgui.Dialog().notification(
            "Shadow Touch",
            "Error fetching movie information",
            xbmcgui.NOTIFICATION_ERROR,
            3000
        )
        return None
    except Exception as e:
        log_error(f"Unexpected error: {str(e)}")
        return None


def set_movie_info_properties(movie_data):
    """
    Set movie info as window properties for skin access

    Args:
        movie_data (dict): Movie data from TMDB API
    """
    if not movie_data:
        return

    window = xbmcgui.Window(10000)  # Home window

    # Basic info
    window.setProperty('ShadowTouch.MovieTitle', movie_data.get('title', ''))
    window.setProperty('ShadowTouch.MoviePlot', movie_data.get('overview', ''))
    window.setProperty('ShadowTouch.MovieRating', str(movie_data.get('vote_average', '0')))
    window.setProperty('ShadowTouch.MovieYear', movie_data.get('release_date', '')[:4] if movie_data.get('release_date') else '')

    # Images
    poster_path = movie_data.get('poster_path')
    if poster_path:
        poster_url = f"{TMDB_IMAGE_BASE_URL}/{TMDB_POSTER_SIZE}{poster_path}"
        window.setProperty('ShadowTouch.MoviePoster', poster_url)

    backdrop_path = movie_data.get('backdrop_path')
    if backdrop_path:
        backdrop_url = f"{TMDB_IMAGE_BASE_URL}/{TMDB_BACKDROP_SIZE}{backdrop_path}"
        window.setProperty('ShadowTouch.MovieBackdrop', backdrop_url)

    # Genres
    genres = movie_data.get('genres', [])
    if genres:
        genre_names = ', '.join([g['name'] for g in genres])
        window.setProperty('ShadowTouch.MovieGenres', genre_names)

    # Runtime
    runtime = movie_data.get('runtime')
    if runtime:
        window.setProperty('ShadowTouch.MovieRuntime', f"{runtime} min")

    # Cast (first 5 actors)
    credits = movie_data.get('credits', {})
    cast = credits.get('cast', [])[:5]
    if cast:
        cast_names = ', '.join([actor['name'] for actor in cast])
        window.setProperty('ShadowTouch.MovieCast', cast_names)

    # Director
    crew = credits.get('crew', [])
    directors = [member['name'] for member in crew if member['job'] == 'Director']
    if directors:
        window.setProperty('ShadowTouch.MovieDirector', directors[0])

    log_info(f"Set movie info properties for: {movie_data.get('title')}")


def show_movie_info_dialog(tmdb_id=None, title=None, year=None):
    """
    Show long-press overlay dialog with movie information

    Args:
        tmdb_id (str/int): TMDB movie ID
        title (str): Movie title
        year (str/int): Movie year
    """
    # Clear previous data
    clear_movie_info()

    # Fetch movie info
    movie_data = get_movie_info(tmdb_id=tmdb_id, title=title, year=year)

    if movie_data:
        # Set properties for skin access
        set_movie_info_properties(movie_data)

        # Open custom dialog
        # This will be handled by DialogVideoInfo.xml in the skin
        xbmc.executebuiltin('ActivateWindow(12003)')  # DialogVideoInfo window ID
    else:
        xbmcgui.Dialog().notification(
            "Shadow Touch",
            "Could not load movie information",
            xbmcgui.NOTIFICATION_WARNING,
            3000
        )


def add_to_watchlist(tmdb_id):
    """
    Add movie to watchlist (placeholder for future implementation)

    Args:
        tmdb_id (str/int): TMDB movie ID
    """
    log_info(f"Add to watchlist: {tmdb_id}")
    xbmcgui.Dialog().notification(
        "Shadow Touch",
        "Watchlist feature coming soon!",
        xbmcgui.NOTIFICATION_INFO,
        2000
    )


def mark_as_watched(tmdb_id):
    """
    Mark movie as watched (placeholder for future implementation)

    Args:
        tmdb_id (str/int): TMDB movie ID
    """
    log_info(f"Mark as watched: {tmdb_id}")
    xbmcgui.Dialog().notification(
        "Shadow Touch",
        "Mark as watched feature coming soon!",
        xbmcgui.NOTIFICATION_INFO,
        2000
    )
