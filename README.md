# Supermarked explorer

> København

Install streamlit and application dependencies:

```bash
pip install streamlit numpy pandas matplotlib seaborn
```

Run supermarkeder:

```bash
# remote (if you did not clone the repository)
streamlit run https://raw.githubusercontent.com/skipperkongen/commercial-explorer/main/supermarked_explorer.py

# local (if you cloned the repository)
streamlit run supermarkeder_kbh.py
```

Run commercial:

```bash
# remote (if you did not clone the repository)
streamlit run https://raw.githubusercontent.com/skipperkongen/commercial-explorer/main/commercial_explorer.py

# local (if you cloned the repository)
streamlit run commercial_kbh.py
```


## Data sources

Data fra OpenStreetMap. eksporteret via Overpass.

- [download url](https://overpass-api.de/api/map?bbox=12.5292,55.6599,12.6433,55.6979)
