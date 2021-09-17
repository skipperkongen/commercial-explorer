# Supermarked explorer

> København edition

This is a short demo of streamlit that visualises shop data from openstreetmap
on a 3D map using pydeck (built into streamlit).

Look at the source code to see how it's made. It's quite simple.

- [commercial_explorer.py](./commercial_explorer.py)
- [supermarked_explorer.py](./supermarked_explorer.py)

## How to run

Install streamlit and application dependencies:

```bash
pip install streamlit numpy pandas matplotlib seaborn
```

Run supermarked explorer:

```bash
# remote (if you did not clone the repository)
streamlit run https://raw.githubusercontent.com/skipperkongen/commercial-explorer/main/supermarked_explorer.py

# local (if you cloned the repository)
streamlit run supermarkeder_kbh.py
```

Run commercial explorer:

```bash
# remote (if you did not clone the repository)
streamlit run https://raw.githubusercontent.com/skipperkongen/commercial-explorer/main/commercial_explorer.py

# local (if you cloned the repository)
streamlit run commercial_kbh.py
```


## Data sources

Data fra OpenStreetMap. eksporteret via Overpass.

- [download url](https://overpass-api.de/api/map?bbox=12.5292,55.6599,12.6433,55.6979)
