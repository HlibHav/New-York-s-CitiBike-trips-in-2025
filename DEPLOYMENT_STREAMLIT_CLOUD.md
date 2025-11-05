# Streamlit Cloud Deployment Guide

## Files Created/Modified for Deployment

1. **`citibike_ultimate_dashboard.py`** - Main application file (copied from `app.py`)
   - This is the file that Streamlit Cloud expects as the main module

2. **`.streamlit/config.toml`** - Streamlit configuration file
   - Sets server settings, theme, and browser preferences

3. **`requirements.txt`** - Updated with `requests` dependency
   - All required Python packages for the application

4. **`.gitignore`** - Git ignore file to exclude unnecessary files from deployment

## Deployment Steps

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Prepare for Streamlit Cloud deployment"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to https://share.streamlit.io/
   - Sign in with GitHub
   - Click "New app"
   - Select your repository: `new-york-s-citibike-trips-in-2025`
   - Set **Main file path**: `citibike_ultimate_dashboard.py`
   - Set **Branch**: `main`
   - Click "Deploy"

## Important Notes

- The data file `data/citibike_weather_detrended_analysis.csv` must be committed to the repository
- If the file is too large (>100MB), consider using Git LFS or Streamlit's file uploader
- The LangChain backend features will not work on Streamlit Cloud unless you deploy the backend separately
- Make sure all CSV files in the `data/` directory are committed to the repository

## Troubleshooting

If deployment fails:
1. Check that `citibike_ultimate_dashboard.py` exists in the root directory
2. Verify `requirements.txt` has all dependencies
3. Ensure data files are in the repository
4. Check Streamlit Cloud logs for specific error messages

