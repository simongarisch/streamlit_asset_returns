# streamlit_asset_returns

A streamlit app for asset returns.

## Running locally
```python
python -m venv env
call "./env/Scripts/activate"
pip install -r requirements.txt
streamlit run main.py
```

## Running with docker
The Dockerfile is configured to run on port 5000.
```bash
./docker_build.sh
./docker_run.sh
```
