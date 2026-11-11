"""Exercise HTTP failure behavior without audio hardware or live requests."""
import ast
from pathlib import Path
import types
import unittest
from unittest.mock import Mock

SOURCE = Path(__file__).resolve().parents[1] / 'Nova Software' / 'web.py'

class WebTests(unittest.TestCase):
    def load_scraper(self, requests):
        tree = ast.parse(SOURCE.read_text())
        functions = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'scrape_text']
        namespace = {'requests': requests}
        exec(compile(ast.Module(body=functions, type_ignores=[]), str(SOURCE), 'exec'), namespace)
        return namespace['scrape_text']
    def test_timeout_returns_none(self):
        class RequestError(Exception): pass
        client = types.SimpleNamespace(RequestException=RequestError, get=Mock(side_effect=RequestError('offline')))
        self.assertIsNone(self.load_scraper(client)('https://example.com'))
        client.get.assert_called_once_with('https://example.com', timeout=10)
    def test_http_error_returns_none(self):
        class RequestError(Exception): pass
        response = Mock(); response.raise_for_status.side_effect = RequestError('404')
        client = types.SimpleNamespace(RequestException=RequestError,get=Mock(return_value=response))
        self.assertIsNone(self.load_scraper(client)('https://example.com'))
    def test_voice_listener_only_runs_as_script(self):
        tree = ast.parse(SOURCE.read_text())
        direct = [n for n in tree.body if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call)]
        self.assertFalse(any(isinstance(n.value.func,ast.Name) and n.value.func.id == 'get_speech_input' for n in direct))
if __name__ == '__main__': unittest.main()
