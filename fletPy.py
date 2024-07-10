import flet as ft
import yaml


def main(page: ft.Page):
    # Открываем и читаем YAML файл
    with open('spoke_tension_tables.yaml', 'r') as file:
        spoke_tension_tables = yaml.safe_load(file)

    page.title = "Калькулятор натяжения спиц"

    def dd_spokes_changed(e):

        # for key, value in spoke_tension_tables[dd_tools.value].items():
            # print(spoke_tension_tables[dd_tools.value][dd_spokes.value])
        tension_values = spoke_tension_tables[dd_tools.value][dd_spokes.value]['Tension']
        readings_values = spoke_tension_tables[dd_tools.value][dd_spokes.value]['Readings']
        print(tension_values)
        print(readings_values)

        column_list = [ft.DataColumn(ft.Text(""))]
        row_tension = [ft.DataCell(ft.Text("Натяжение"))]
        row_readings = [ft.DataCell(ft.Text("Значение"))]

        for col in range(len(tension_values)):
            column_list.append(ft.DataColumn(ft.Text(""), numeric=True))
            row_tension.append(ft.DataCell(ft.Text(tension_values[col])))
            row_readings.append(ft.DataCell(ft.Text(readings_values[col])))

        table_readings = ft.DataTable(
            columns=column_list,
            rows=[
                ft.DataRow(
                    cells=row_tension
                ),
                ft.DataRow(
                    cells=row_readings
                )
            ]
        )
        page.add(table_readings, ft.Divider())


    def dd_tools_changed(e):
        print(dd_tools.value)
        # spokes_list = []
        for key in spoke_tension_tables[dd_tools.value].keys():
            # spokes_list.append(ft.dropdown.Option(key))
            dd_spokes.options.append(ft.dropdown.Option(key))

        # print(type(print(type(spoke_tension_tables[dd_tools.value].keys()))))
        # print(spoke_tension_tables[dd_tools.value])
        # spokes_list = list(spoke_tension_tables[dd_tools.value].keys())
        # dd_spokes = ft.Dropdown(
        #     on_change=dd_spokes_changed,
        #     autofocus=True,
        #     border_radius=10,
        #     elevation=10,
        #     label="Спицы",
        #     width=200,
        #     options=spokes_list,
        #)
        page.add(dd_spokes)


    tools_list = list()
    for key in spoke_tension_tables.keys():
        tools_list.append(ft.dropdown.Option(key))
        # spokes_list.append(ft.dropdown.Option(value['Spokes']))
        # print(value['Main']['Description'])

    dd_tools = ft.Dropdown(
        on_change=dd_tools_changed,
        autofocus=True,
        border_radius=ft.border_radius.all(10),
        # padding=ft.padding.only(left=10),
        elevation=10,
        label="Инструмент",
        width=max(len(str(s)) for s in tools_list) * 10,
        options=tools_list,
    )

    spokes_list = []
    # for key in spoke_tension_tables[dd_tools.value].keys():
    #     spokes_list.append(ft.dropdown.Option(key))
    dd_spokes = ft.Dropdown(
        on_change=dd_spokes_changed,
        autofocus=True,
        border_radius=10,
        elevation=10,
        label="Спицы",
        width=200,
        options=spokes_list,
    )
    # for key in spoke_tension_tables:
    #     dd_tools.options.append(ft.dropdown.Option(key.Description))

    page.add(dd_tools)



ft.app(target=main)