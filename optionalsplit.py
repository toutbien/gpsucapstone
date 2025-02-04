# Stored in the same dir as your JSON file needing split
import json

def split_large_json(input_file, output_prefix="part_", chunk_size=1000):
    """
    Splits a large JSON file containing a list of objects into smaller chunks.

    Parameters:
    - input_file (str): Path to the large JSON file.
    - output_prefix (str): Prefix for output files.
    - chunk_size (int): Number of JSON objects per split file.
    """
    try:
        # Load the large JSON file
        with open(input_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Ensure the JSON is a list
        if not isinstance(data, list):
            raise ValueError("JSON file must contain a list of objects.")

        # Split into chunks
        total_chunks = (len(data) // chunk_size) + (1 if len(data) % chunk_size > 0 else 0)
        for i in range(total_chunks):
            chunk = data[i * chunk_size : (i + 1) * chunk_size]
            output_file = f"{output_prefix}{i+1}.json"
            
            with open(output_file, "w", encoding="utf-8") as out_file:
                json.dump(chunk, out_file, indent=4)
            
            print(f"Created: {output_file} ({len(chunk)} entries)")

        print(f"✅ Successfully split into {total_chunks} files.")

    except Exception as e:
        print(f"❌ Error: {e}")

# Example usage:
# split_large_json("large_file.json", output_prefix="split_", chunk_size=500)
