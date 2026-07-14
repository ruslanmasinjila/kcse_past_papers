import sys
import os
import img2pdf

def merge_png_to_pdf():
    # 1. Validate the command-line argument
    if len(sys.argv) < 2:
        print("Error: Please provide the total number of files 'n'.")
        print("Usage: python png_to_pdf.py <integer_n>")
        sys.exit(1)
        
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: The argument 'n' must be an integer.")
        sys.exit(1)

    # 2. Get the directory where this script is physically located
    # This ensures it always looks in its own folder, regardless of where you call it from.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 3. Build the sorted list of file paths based on your sequential naming
    file_list = []
    for i in range(1, n + 1):
        filename = f"{i}.png"
        full_path = os.path.join(current_dir, filename)
        
        # Check if the file actually exists before adding it
        if os.path.exists(full_path):
            file_list.append(full_path)
        else:
            print(f"Warning: Expected file '{filename}' was not found. Skipping.")

    if not file_list:
        print("Error: No valid PNG files found to convert.")
        sys.exit(1)

    # 4. Convert and write to output.pdf in the same directory
    output_pdf_path = os.path.join(current_dir, "output.pdf")
    
    print(f"Converting and merging {len(file_list)} images into 'output.pdf'...")
    
    try:
        with open(output_pdf_path, "wb") as f:
            f.write(img2pdf.convert(file_list))
        print("Success! 'output.pdf' has been created.")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

if __name__ == "__main__":
    merge_png_to_pdf()