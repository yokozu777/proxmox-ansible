import re

# Define the path to the JS file
js_file_path = '/usr/share/pve-manager/js/pvemanagerlib.js'

# Define the thermal object to insert
thermal_object = """
{
    itemId: 'thermal',
    colspan: 2,
    printBar: false,
    title: gettext('Thermal State(℃)'),
    textField: 'thermalstate',
    renderer:function(value){
        const cpu_temp_arr = JSON.parse(value);
        const sections = [];
        for (const [dev, arr] of Object.entries(cpu_temp_arr)) {
            for (const [name, temps] of Object.entries(arr)) {
                if (name === 'Adapter') {
                    continue;
                }
                for (const [temp_name, temp] of Object.entries(temps)) {
                    if (temp_name.includes("_input")) {
                        sections.push(dev.split('-')[0] + ": " + temp);
                        break;
                    }
                }
                break;
            }
        }
        return sections.join(", ");
    }
},
"""

# Read the content of the JS file
with open(js_file_path, 'r') as file:
    content = file.read()

# Print the first 500 characters of the content to verify the file is read correctly
print("Original content before modification (JS file):")
print(content[:500])  # Print only the first 500 characters for readability

# Check if the thermal_object already exists in the file
if thermal_object.strip() not in content.strip():
    # Modify content: insert thermal object before itemId: 'version'
    # Match the line containing itemId: 'version' and insert thermal_object before it
    modified_content = re.sub(r'(\s*{\s*itemId:\s*\'version\')', thermal_object + r'\1', content)

    # Print the modified content for debugging
    print("\nModified content after modification (JS file):")
    print(modified_content[:500])  # Print only the first 500 characters for readability

    # Write the modified content back to the file
    with open(js_file_path, 'w') as file:
        file.write(modified_content)

    print("Insertion of thermal object before 'itemId: version' completed (JS file).")
else:
    print("Thermal object already exists, skipping insertion.")

# Define the path to the Perl file
perl_file_path = '/usr/share/perl5/PVE/API2/Nodes.pm'

# Define the line to insert
line_to_insert = "$res->{thermalstate} = `sensors -j`;"

# Read the content of the Perl file
with open(perl_file_path, 'r') as file:
    content = file.read()

# Print the first 500 characters of the content to verify the file is read correctly
print("Original content before modification (Perl file):")
print(content[:500])  # Print only the first 500 characters for readability

# Check if the line already exists (including stripping extra spaces)
if line_to_insert.strip() not in content.strip():
    # Modify content: insert the line after 'PVE::pvecfg::version_text();'
    # We match the line containing 'PVE::pvecfg::version_text();' and insert line_to_insert after it
    modified_content = re.sub(r'(PVE::pvecfg::version_text\(\);)', r'\1\n' + line_to_insert, content)

    # Print the modified content for debugging
    print("\nModified content after modification (Perl file):")
    print(modified_content[:500])  # Print only the first 500 characters for readability

    # Write the modified content back to the file
    with open(perl_file_path, 'w') as file:
        file.write(modified_content)

    print("Insertion of thermalstate line after 'PVE::pvecfg::version_text();' completed (Perl file).")
else:
    print("Line already exists, skipping insertion.")
