# Medical Assistant — RAG over a Clinical Reference Manual

**Course:** Natural Language Processing with Generative AI · **Score:** 109/110 · **Type:** Retrieval-augmented generation

---

## Business context

Clinicians need fast, accurate answers from dense reference material. A general-purpose LLM will answer fluently and sometimes wrongly — and in a clinical context, a confident wrong answer is worse than no answer.

Retrieval-augmented generation addresses this directly: ground every response in retrieved passages from an authoritative source, so the model is summarising a document rather than recalling from its weights.

## Objective

Build a question-answering assistant over a medical diagnosis manual, where responses are traceable to source passages.

## Data

`medical_diagnosis_manual.pdf` — a clinical reference manual (~19 MB).

> **The source PDF is not redistributed here.** It is third-party course material.

## Approach

- **Document ingestion** — PDF parsing and text extraction.
- **Chunking** — splitting into passages with overlap, sized against the embedding model's context window.
- **Embedding** — sentence-transformer embeddings for each chunk.
- **Vector store** — indexed for similarity search.
- **Retrieval + generation** — top-k retrieval on the query, retrieved context passed to the generation step with a prompt constraining the model to the supplied context.
- **Evaluation** — response quality assessed against known-answer queries.

## What actually mattered

**Chunking strategy dominated everything else.** Chunk boundaries that split a clinical procedure or a differential diagnosis list mid-way produced retrievals that were topically relevant and clinically wrong. Fixing the chunking improved answer quality more than any change to the embedding model or the prompt.

This is the project closest to my day job. Strip away the LLM and it's a pipeline problem: ingest, transform, index, serve. The failure modes are the failure modes of any ETL system — bad boundaries, silent truncation, stale indexes.

## Files

```
notebooks/  Full_Code_NLP_RAG_Project_Notebook.ipynb
data/       (source PDF not committed - see above)
reports/    Business Context.docx, Rubric.docx
```
