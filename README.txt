Machine Learning Project 23/24

Group Members:

- Inês Sá Pereira Estevão Gaspar (up202007210@edu.fe.up.pt)
- Lourenço Alexandre Correia Gonçalves (up202004816@edu.fe.up.pt)
- Pedro Pereira Ferreira (up202004986@edu.fe.up.pt)

Instructions:

- The `data` folder contains the datasets used in the project, during the data understanding and cleaning phase.

- The main scripts are in the `scripts` folder. There are 2 subfolders, besides the populate and cleaning script (just for the `teams` table):

    - analysis: contains the scripts used to perform the data analysis and cleaning.
    - classification: contains the scripts used to perform the classification tasks.

- To run the classification, just select the desired script in your IDE and run it in the project's root directory. The script will perform the classification and print the results.

- In case you need to install any library, just run `pip install -r requirements.txt` in the project's root directory console.

- If you want to run the merge process, follow these steps:
    - open the Rapidminer;
    - select `Import process`;
    - select the `merge.rmp` file;
    - import each of the datasets;
    - run the process.