# UOCIS322 - Project 6 #
Cheyanne Kester
This project expands on Project 5 with the addition of a RESTful API!

To use docker compose to build and run this project:
Navigate in your terminal to the project-6 main directory
`docker compose up --build` (you may add `-d` to the end if you wish to use detached mode)
then navigate to `localhost:5002`

To turn the project off:
`^C`
`docker compose down`

## The Application - Breakdown
P4: This is an application to calculate and display the Open and Close times of checkpoints along a bicycle race of a certain distance, called the Brevet distance. A user should be able to select their desired Brevet distance by using the `Distance` drop down menu, and select their start date and time using the box with the words `Begins at` next to it. After the user has made these selections, they can then input checkpoints in the `Km` or `Miles` column, and the application will display the Open and Close date and times for each checkpoint. 

P5: With the new database functionality, we have two new buttons: `Display` and `Submit`.
`Display` will pull the most recent table from the mongo database, and fill in the values on the webpage without a reload.
`Submit` will take the current table on the webpage, and insert it into the database, then clear the webpage's table, without reloading. 

P6: We replace the database interaction in `/brevets` with an all-new API in the `/api` directory. This includes two resources: `Brevet` and `Brevets` in the `/api/resources` folder, as well as two models `Brevet` and `Checkpoint` in `models.py`. 


## What we had to do
### Write Tests 
P4: Firstly, we must write 5 test cases in `test_acp_times.py` for the algorithm file `acp_times.py`. I followed the procedure that Ali showed us in lab on Friday the 17th. I made a test function for each possible brevet distance, and within each I tested checkpoints for every 50 km. For example, the test for brevet 1000 tested 21 different checkpoints.

P5: Secondly, we had to write 2 tests in `test_mypymongo.py` for the database interaction file `mypymongo.py`. I once again followed the general hints that Ali gave in lab, and was able to copy and alter some code from `test_acp_times.py`. The first test is to ensure the `brevet_insert` function properly inserts a table into the database, by checking that the tabke was assigned an id by MongoDB. The second test is to ensure the `bevet_find` function properly fetches the most recent table from the database, this test was essentially identical to the previous one, starting with inserting a table to the db, but instead of checking the id of the table we insert, we made sure the fetched table was the same as the one we inserted.

P6: Did not require new tests, and in fact deleted the `test_mypymongo.py` file. 

To execute these tests, follow this procedure: 
`docker compose up --build -d`
`docker compose exec [SERVICENAME] bash` (my service name is `brevets`; this opens a bash inside the service)
`sed -i -e 's/\r$//' run_tests.sh` (this prevents weird error, might not be necessary for you)
`./run_tests.sh`


### Implement Algorithm & Database Interactions
P4: We had to implement the algorithm in `acp_times.py` so that it would pass the test cases we made. 
The general idea is that for every checkpoint past a certain number of km (200 km for open time and 600km for close time) we had to incrementally calculate the start and close times. By this I mean that, for open time, every 200 km chunk up to the checkpoint distance had to use a different speed; and for close time, every 600km chunk had to use a different speed. A great example of this is `Example 3` on the website https://rusa.org/pages/acp-brevet-control-times-calculator. 

P5: Next, we had to implement the `brevet_insert` and `brevet_find` functions in `mypymongo.py`. I was able to copy and modify the `insert_todo` and `get_todo` functions in the example ToDoListApp's `flask_todo.py`. 

P6: As stated above, We replaced the database interaction in `/brevets` with an all-new API in the `/api` directory. This includes two resources: `Brevet` and `Brevets` in the `/api/resources` folder, as well as two models `Brevet` and `Checkpoint` in `models.py`.


### Update Frontend
P4: We had to modify the `calc.html` file to send the start time (in the "Begins at" box) and the Brevet distance (in the Distance box) to `flask_brevets.py`. 

P5: We had to modify the `calc.html` file to have two new buttons, `Display` and `Submit`, and configure their interactions send the proper data to `flask_brevets.py`.

### Update Flask to accept the new start time and brevet distance
P4: Lastly, we had to modify `flask_brevets.py` to accept the start time and brevet distance. I did this by using `request.args.get(what I need)`, as the given code did with getting `km`. Once the file was accepting the arguments, I had to modify a couple of the given code's lines to ensure that start time and brevet distance were being passed into `acp_times.py` correctly. 

P5: Modify `flask_brevets.py` to accept insert_brevet and fetch_brevet requests from `calc.html`.

P6: Did not require much front-end updating besides changing variable names. 

## Authors of Original Overview and Project 
### (Content from Original README deleted for simplicity)

Michal Young, Ram Durairajan. Updated by Ali Hassani.
