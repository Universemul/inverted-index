# Inverted-index
Python package providing an in-memory Inverted Index


# Features

- Documents Indexing
  - [X] Insert a document or a bulk
  - [X] Remove a document by `id`
  - [X] Persistence of disk (using existing config or config created by the developer)
- Search documents
  - [X] By exact match
  - [ ] Using filtering on field (like `AND`, `OR`, `NOT`, ...)
  - [ ] Using fuzzy search 
  - [ ] Using regex
- [ ] Tokenizer
  - [ ] French
  - [ ] Other language
- [ ] Stemming
  - [ ] French
  - [ ] Other language
- [ ] Stopwords
  - [ ] French
  - [ ] Other language
- [ ] Better default serialization. Partial json update instead of overriding the whole file
- [ ] L4Z Configuration
