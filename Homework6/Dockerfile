# docker image build -t python4ai-2022-project .
# docker rm python4ai
# docker run --name python4ai python4ai-2022-project
# or 
# docker run --name python4ai dgofman/python4ai-2022-project > qin790_output.txt

FROM continuumio/miniconda3

RUN conda create -n mro_env -c conda-forge python=3.7 PyPDF2 pattern nltk

RUN echo "source activate mro_env" > ~/.bashrc
ENV PATH /opt/conda/envs/mro_env/bin:$PATH

RUN python -c "import nltk; nltk.download('all')"

COPY SampleCh7.pdf Samplech7.pdf
COPY project.py .

CMD ["python", "project.py"]