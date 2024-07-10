import flet as ft
import yaml


def main(page: ft.Page):
    # Открываем и читаем YAML файл
    with open('spoke_tension_tables.yaml', 'r') as file:
        spoke_tension_tables = yaml.safe_load(file)

    page.title = "Калькулятор натяжения спиц"

    def update_table(tool, spoke):
        tension_values = spoke_tension_tables[tool][spoke]['Tension']
        readings_values = spoke_tension_tables[tool][spoke]['Readings']

        columns = [ft.DataColumn(ft.Text(""))] + [ft.DataColumn(ft.Text(""), numeric=True) for _ in tension_values]
        row_tension = [ft.DataCell(ft.Text("Натяжение"))] + [ft.DataCell(ft.Text(value)) for value in tension_values]
        row_readings = [ft.DataCell(ft.Text("Значение"))] + [ft.DataCell(ft.Text(value)) for value in readings_values]

        table_readings = ft.DataTable(
            columns=columns,
            rows=[
                ft.DataRow(cells=row_tension),
                ft.DataRow(cells=row_readings)
            ]
        )
        return table_readings

    def dd_spokes_changed(e):
        selected_tool = dd_tools.value
        selected_spoke = dd_spokes.value
        table = update_table(selected_tool, selected_spoke)
        page.controls.clear()
        page.add(dd_tools, dd_spokes, table)
        page.update()

    def dd_tools_changed(e):
        selected_tool = dd_tools.value
        dd_spokes.options = [ft.dropdown.Option(spoke) for spoke in spoke_tension_tables[selected_tool].keys()]
        dd_spokes.update()

    tools_list = [ft.dropdown.Option(tool) for tool in spoke_tension_tables.keys()]

    dd_tools = ft.Dropdown(
        on_change=dd_tools_changed,
        autofocus=True,
        border_radius=ft.border_radius.all(10),
        elevation=10,
        label="Инструмент",
        width=200,
        options=tools_list,
    )

    dd_spokes = ft.Dropdown(
        on_change=dd_spokes_changed,
        autofocus=True,
        border_radius=10,
        elevation=10,
        label="Спицы",
        width=200,
        options=[],
    )

    page.add(dd_tools, dd_spokes)


ft.app(target=main)
