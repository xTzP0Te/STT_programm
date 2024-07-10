import yaml

# Откройте и прочитайте YAML файл
with open('spoke_tension_tables.yaml', 'r') as file:
    spoke_tension_tables = yaml.safe_load(file)

print(spoke_tension_tables)
# print(spoke_tension_tables.keys()[0])
for key, value in spoke_tension_tables.items():
    print(value['Main']['Description'])