"""Regression for the web GUI callback without devices or a display server."""
import ast
from pathlib import Path
import types
import unittest
from unittest.mock import Mock

SOURCE = Path(__file__).resolve().parents[1] / 'Nova Software' / 'web.py'

class ResultTests(unittest.TestCase):
    def callback(self, result):
        tree = ast.parse(SOURCE.read_text())
        node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'scrape_website')
        widget = Mock()
        namespace = {'text_output': widget, 'scrape_text': Mock(return_value=result),
                     'speak': Mock(), 'tk': types.SimpleNamespace(END='end')}
        exec(compile(ast.Module(body=[node], type_ignores=[]), str(SOURCE), 'exec'), namespace)
        return namespace, widget

    def test_success_keeps_result_visible(self):
        namespace, widget = self.callback('Readable article')
        root = Mock()
        namespace['scrape_website']('https://example.com', root)
        widget.insert.assert_called_once_with('end', 'Readable article')
        widget.config.assert_called_with(state='disabled')
        root.destroy.assert_not_called()

    def test_failure_keeps_diagnostic_visible(self):
        namespace, widget = self.callback(None)
        root = Mock()
        namespace['scrape_website']('https://example.com', root)
        self.assertIn('Failed', widget.insert.call_args.args[1])
        root.destroy.assert_not_called()

    def test_empty_input_does_not_request_network(self):
        namespace, widget = self.callback(None)
        root = Mock()
        namespace['scrape_website']('', root)
        namespace['scrape_text'].assert_not_called()
        self.assertIn('enter', widget.insert.call_args.args[1])
        root.destroy.assert_not_called()

if __name__ == '__main__':
    unittest.main()
