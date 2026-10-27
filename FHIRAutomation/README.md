1. create virtua env - python3 -> m venv .venv
2. activate virtual env -> source .venv/bin/activate
3. Run requirements txt - pip install -r requirements.txt

Functionality:

1. A document that contains fields that are compulsory. this documents fields are present dept wise.
2. Let say we have Insurance -> Careplan -> CareTeam
3. If a field is not present dept wise, them it needs to be passed back to preceeding dept with a summary about which fields are not present or need more data.

4. Existing workflow -> A person either practitioner or his behalf, used to manually check all field like blood test, urine test etc and if any of it was not present then he used to reach them specifying missing on incomplete details.

5. We automated this flow using LangChain, LangGraph and LLM. If a field is not present or has incomplete data then LLM used to flag it and write a summary that all this fields were supposed to be present. Before giving it over, humanr review is there.

6. What information should be atleast present in fields comes from a database and it is verified.