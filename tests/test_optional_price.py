"""Focused regression tests for optional appointment prices.

Run from the repository root:
    python -m unittest discover -s tests -v

GUI methods are exercised with a small fake Treeview, so no display is required.
"""

import unittest
from unittest.mock import Mock

from controller.app_controller import AppController
from view.main_view import MainView
from view.report_view import ReportView


def appointment(price):
    return (
        1,
        "Test Customer",
        "21999999999",
        "test@example.com",
        "2026-11-01 14:00:00",
        price,
        "Hair",
    )


class FakeTree:
    def __init__(self):
        self.items = []

    def get_children(self):
        return []

    def delete(self, _item):
        pass

    def insert(self, _parent, _index, *, values, **_kwargs):
        self.items.append(values)


class OptionalPriceTests(unittest.TestCase):
    def test_list_displays_missing_price(self):
        view = MainView.__new__(MainView)
        view.tree = FakeTree()
        view.populate_treeview([appointment(None)])
        self.assertEqual(view.tree.items[0][4], "-")

    def test_report_displays_missing_price(self):
        view = ReportView.__new__(ReportView)
        view.tree = FakeTree()
        view.populate_report([appointment(None)])
        self.assertEqual(view.tree.items[0][5], "-")

    def test_edit_form_handles_missing_price(self):
        controller = AppController.__new__(AppController)
        controller.selected_id = 1
        controller.model = Mock()
        controller.model.get_agendamento_by_id.return_value = appointment(None)
        controller.main_view = Mock()

        controller.handle_edit_selection()

        form_data = controller.main_view.set_form_data.call_args.args[0]
        self.assertEqual(form_data["Valor"], "")

    def test_known_prices_keep_two_decimals(self):
        list_view = MainView.__new__(MainView)
        list_view.tree = FakeTree()
        list_view.populate_treeview([appointment(42.5)])
        self.assertEqual(list_view.tree.items[0][4], "42.50")

        report_view = ReportView.__new__(ReportView)
        report_view.tree = FakeTree()
        report_view.populate_report([appointment(42.5)])
        self.assertEqual(report_view.tree.items[0][5], "42.50")


if __name__ == "__main__":
    unittest.main()
