## 📖Introduction
The github code is the code for the data processing web for **CSCWD 2022** paper [Representation and Extraction of Physics Knowledge Based on Knowledge Graph and Embedding-Combined Text Classification for Cooperative Learning](https://ieeexplore.ieee.org/abstract/document/9776230/), supported by ZJU SRTPX0522 foundations.

## ✈️ Data Processing

See the directory `Gaokao-Physics-Data-Fetching/`.

### Web Crawling

We modified the web crawling code from https://github.com/Alex-gousheng/BaiduWenkuSpider.

We crawled data from Baidu Wenku for high school physical knowledge documents. The code can be found at `Scrapy_bd.py`. The script utilizes the functionality of the **Scrapy framework** to systematically crawl entries related to college entrance exam physics from the Baidu encyclopedia to provide data support for the construction of the knowledge graph. Those `.docx` file should be furtherly converted to `.txt` file.

### Data Labelling

Run the code according to the following order.

- `Path_Walk.py`: Convert `.docx` file to `.txt` file.
- `Data_Incising.py`: Split and sample the content of the captured data files, and save the sampled content as a separate text file to form a new data set.
- `knowledge_filter.py`: Filtered out the magic characters in the text.
- `extract_keyword.py`: Build a TF-IWF model of keywords for specialized documents and generate a dictionary of keyword sequences for each knowledge point.
- `Tagging.py`: Classify and label the captured physical knowledge point data, save it to a new dataset, and add labels to each file.

### Train/Validation/Test Dataset Split

We sort the data in valid(dev)/test/train set, the ratio is 8:1:1. The code can be found at `BGM.py`. 
