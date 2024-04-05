from flask import Flask, render_template
import csv

app = Flask(__name__)

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

@app.route('/')
def index():
    csv_data = read_csv('data.csv')  # Assuming data.csv is the CSV file containing your data
    return render_template('index3.html', data=csv_data)

app.run(debug=True)

# # Define the path to your file
# file_path = os.path.join(app.root_path, 'results.csv')

# def read_csv(file_path):
#     # Read the CSV file using pandas
#     df = pd.read_csv(file_path)
#     return df

# @app.route('/')
# def index():
#     # Call the read_csv function with the file path
#     data = read_csv(file_path)
#     # Now you can use the data or perform any other operations
#     return f'Data loaded from CSV: {data.head()}'

# if __name__ == '__main__':
#     app.run(debug=True)
# import os
# import csv
# from flask import Flask, render_template

# app = Flask(__name__)

# # Define the path to your file
# file_path = os.path.join(app.root_path, 'results.csv')

# def read_csv(file_path):
#     data = []
#     with open(file_path, 'r') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             data.append(row)
#     return data

# @app.route('/')
# def index():
#     # Call the read_csv function with the file path
#     csv_data = read_csv(file_path)
#     # Now you can use csv_data or perform any other operations
#     return render_template('index3.html', data=csv_data)

# if __name__ == '__main__':
#     app.run(debug=True)
