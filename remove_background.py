from rembg import remove

input_path = 'image_input.png'
output_path = 'image_output.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)