from fastapi import FastAPI, responses
import os

app = FastAPI()

log = ""

@app.get("/download")
def downloadfile(url="", name = ""):
    os.system("wget -O" + name + "'" + url + "'")
    log = "Download Complete: " + name + " From: " + url
    return responses.PlainTextResponse("OK")

@app.get("/log")
def returnlog():
    log2 = log
    log = ""
    return responses.PlainTextResponse(log2)

@app.get("/reduce")
def reduceFileSize(name = ""):
    with open(name, 'rb') as input_file:
        # Read the binary data from the file
        binary_data = input_file.read()

        # Convert the binary data to an integer
        binary_as_integer = int.from_bytes(binary_data, byteorder='big')

        # Perform a right shift by 3 positions (divide by 8)
        result_integer = binary_as_integer >> 6

        # Convert the result back to binary data
        result_binary_data = result_integer.to_bytes((result_integer.bit_length() + 7) // 8, byteorder='big')

        # Create the output file name
        output_name = name + ".reduced"

        # Write the result to the output binary file
        with open(output_name, 'wb') as output_file:
            output_file.write(result_binary_data)

    return responses.PlainTextResponse("COMPLETE")

@app.get("/getfile")
def downloadfile(name = ""):
    return responses.PlainTextResponse(open(name + ".reduced", "rb").read())
