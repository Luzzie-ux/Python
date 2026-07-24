# Ex00

## Set up the following architecture:
    
    •An abstract class DataProcessor that inherits from ABC and defines the common processing interface.
    
    •Three specialized classes NumericProcessor, TextProcessor, and LogProcessor that inherit from the DataProcessor class and will process different kinds of data.
    
    •Two abstract methods in DataProcessor: validate, which will check whether the input data are appropriate for the current data processor, and ingest, which will process the input data. Each specialized class will need to override these methods.
    
    •One standard method in DataProcessor: output, which will output ingested data.

## You need to comply with the following constraints:
    
    •The validate method will be defined as validate(self, data: Any) -> bool in the DataProcessor class. The overriding methods in the specialized classes will share the same signature, as they cannot know what data will be sent and must accept any type. This method returns a bool that indicates if the provided data can be ingested by this data processor.

    •The ingest method will be defined as ingest(self, data: Any) -> None in the DataProcessor class. The overriding methods in the specialized classes will have their own specific signatures to match the types they expect. In case the user does not validate the data before calling ingest, and provides invalid data, an exception must be raised.
    
    •The output method will be defined as output(self) -> tuple[int, str] in the DataProcessor class. There is no need to override it in the specialized classes.

    •The NumericProcessor ingests int, float, and lists of both types (including mixed-type lists). It then converts the data into strings and stores it internally (keeping each item separated), waiting to be extracted piece by piece using the output method. The overriding ingest method signature must reflect the accepted types.

    •The TextProcessor ingests str and lists of strings. It stores the data internally (keeping each item separated), waiting to be extracted piece by piece using the output method. The overriding ingest method signature must reflect the accepted types.

    •The LogProcessor ingests a dict of string key-value pairs, and lists of that type. It then converts the data into strings and stores it internally (keeping each item separated), waiting to be extracted piece by piece using the output method. The overriding ingest method signature must reflect the accepted types.

    •The output method will extract the oldest piece of data stored internally in the data processor, along with the associated processing rank within the data processor. The piece of data is then removed from the data processor.

## Finally, test your architecture:

    •Create instances for each specialized class.

    •Test valid and invalid data for each class through the validate method.

    •Test at least one invalid data item with the ingest method without prior validation, and check that it raises an exception. This will leave you with a mypy warning, on purpose.

    •Ingest various data for each data processor and then extract it using output.

### Example:
```bash
$> python3 data_processor.py
=== Code Nexus - Data Processor ===

Testing Numeric Processor...
Trying to validate input '42': True
Trying to validate input 'Hello': False
Test invalid ingestion of string 'foo'without prior validation:
Got exception: Improper numeric data
Processing data: [1, 2, 3, 4, 5]
Extracting 3 values...
Numeric value 0: 1
Numeric value 1: 2
Numeric value 2: 3

Testing Text Processor...
Trying to validate input '42': False
Processing data: ['Hello', 'Nexus', 'World']
Extracting 1 value...
Text value 0: Hello

Testing Log Processor...
Trying to validate input 'Hello': False
Processing data: [{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, {'log_level': 'ERROR
', 'log_message': 'Unauthorized access!!'}]
Extracting 2 values...
Log entry 0: NOTICE: Connection to server
Log entry 1: ERROR: Unauthorized access!!
```

# Ex01

## Use your code from Exercise 0 and improve it:

	•Create a DataStream class that will receive a stream of data containing different types and then will route each element to the appropriate data processor using polymorphic behavior.

	•This class will implement the def register_processor(self, proc: DataProcessor) -> None: method that allows you to register a new data processor to process the data stream.

	•This class will implement the def process_stream(self, stream: list[typing.Any]) -> None: method that will analyze each element of the list received as a parameter and send it to the appropriate registered data processor. Error messages will be printed if no data processor can handle an element.

	•Finally, the class will implement the def print_processors_stats(self) -> None: method in order to print stream statistics.

	•Create a test scenario that demonstrates the correct processing of a data stream. Display statistics on registered data processors, consume elements using the output method of each data processor and show updated statistics.

### Example:
```bash
$> python3 data_stream.py
=== Code Nexus - Data Stream ===

Initialize Data Stream...
== DataStream statistics ==
No processor found, no data

Registering Numeric Processor

Send first batch of data on stream: ['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING', '
	log_message': 'Telnet access! Use ssh instead'}, {'log_level': 'INFO', 'log_message': 'User wil is
	connected'}], 42, ['Hi', 'five']]
DataStream error - Can't process element in stream: Hello world
	DataStream error - Can't process element in stream: [{'log_level': 'WARNING', 'log_message': 'Telnet
	access! Use ssh instead'}, {'log_level': 'INFO', 'log_message': 'User wil is connected'}]
DataStream error - Can't process element in stream: ['Hi', 'five']

== DataStream statistics ==
Numeric Processor: total 4 items processed, remaining 4 on processor

Registering other data processors
Send the same batch again
== DataStream statistics ==
Numeric Processor: total 8 items processed, remaining 8 on processor
Text Processor: total 3 items processed, remaining 3 on processor
Log Processor: total 2 items processed, remaining 2 on processor

Consume some elements from the data processors: Numeric 3, Text 2, Log 1
== DataStream statistics ==
Numeric Processor: total 8 items processed, remaining 5 on processor
Text Processor: total 3 items processed, remaining 1 on processor
Log Processor: total 2 items processed, remaining 1 on processor
```

### Do you know?
	How does polymorphism allow the DataStream to handle different data types   
	in the stream without knowing their specific implementations?  
	What are the benefits of this design approach?  

# *Ex02

    Use your code from Exercise 1 and improve it in order to obtain a complete data pipeline. Your DataStream class already handles input streams correctly. You need now to handle the output part of the pipeline. This will be achieved by using a plugin system for export classes, made export-compatible through duck typing.

## Implement the following:

    •A new ExportPlugin class that inherits from the special Protocol class.
    
    •This class will define the following method, which will act as a constraint for each export plugin:
        def process_output(self, data: list[tuple[int, str]]) -> None:
    The type of the data parameter is a list of tuples that matches the return value of the output method from the DataProcessor class.

    •The DataStream class will now implement the
        def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
    method, to be used after calling process_stream, that will consume nb elements from all registered data processors and export them using the provided compatible plugin.

    •Create at least a CSV export plugin and a JSON export plugin. No need to use a specific import for these plugins, manually create valid CSV and JSON strings

### Example:
```bash
$> python3 data_pipeline.py
=== Code Nexus - Data Pipeline ===

Initialize Data Stream...

== DataStream statistics ==
No processor found, no data

Registering Processors

Send first batch of data on stream: ['Hello world', [3.14, -1, 2.71],
    [{'log_level': 'WARNING', ' log_message': 'Telnet access! Use ssh instead'},
    {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
    42, ['Hi', 'five']]

== DataStream statistics ==
Numeric Processor: total 4 items processed, remaining 4 on processor
Text Processor: total 3 items processed, remaining 3 on processor
Log Processor: total 2 items processed, remaining 2 on processor

Send 3 processed data from each processor to a CSV plugin:
CSV Output:
3.14,-1,2.71
CSV Output:
Hello world,Hi,five
CSV Output:
WARNING: Telnet access! Use ssh instead,INFO: User wil is connected

== DataStream statistics ==
Numeric Processor: total 4 items processed, remaining 1 on processor
Text Processor: total 3 items processed, remaining 0 on processor
Log Processor: total 2 items processed, remaining 0 on processor

Send another batch of data: [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
    [{'log_level': ' ERROR','log_message': '500 server crash'},
    {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}],
    [32, 42, 64, 84, 128, 168], 'World hello']

== DataStream statistics ==
Numeric Processor: total 11 items processed, remaining 8 on processor
Text Processor: total 7 items processed, remaining 4 on processor
Log Processor: total 4 items processed, remaining 2 on processor

Send 5 processed data from each processor to a JSON plugin:
JSON Output:
    {"item_3": "42", "item_4": "21", "item_5": "32", "item_6": "42", "item_7": "64"}
JSON Output:
    {"item_3": "I love AI", "item_4": "LLMs are wonderful", "item_5": "Stay healthy", "item_6": "World hello "}
JSON Output:
    {"item_2": "ERROR: 500 server crash", "item_3": "NOTICE: Certificate expires in 10 days"}

== DataStream statistics ==
Numeric Processor: total 11 items processed, remaining 3 on processor
Text Processor: total 7 items processed, remaining 0 on processor
Log Processor: total 4 items processed, remaining 0 on processor
```