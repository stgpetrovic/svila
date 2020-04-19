import unittest

from vrijeme import Vrijeme
from vrijeme import Emisija


class TestVrijeme(unittest.TestCase):
    def test_repr(self):
        v = Vrijeme(17, 3, 23)
        self.assertEqual(repr(v), "17:03:23")

    def test_krivi_tip_sat(self):
        with self.assertRaises(TypeError):
            Vrijeme('a', 1, 1)

    def test_krivi_tip_minuta(self):
        with self.assertRaises(TypeError):
            Vrijeme(1, 'a', 1)

    def test_krivi_tip_sekunda(self):
        with self.assertRaises(TypeError):
            Vrijeme(1, 1, 'a')

    def test_preveliki_broj_sat(self):
        with self.assertRaises(ValueError):
            Vrijeme(25, 1, 1)

    def test_preveliki_broj_minuta(self):
        with self.assertRaises(ValueError):
            Vrijeme(1, 61, 1)

    def test_preveliki_broj_sekunda(self):
        with self.assertRaises(ValueError):
            Vrijeme(1, 1, 62)

    def test_usporedbe(self):
        self.assertLess(Vrijeme(12, 0, 0), Vrijeme(14, 0, 0))
        self.assertGreater(Vrijeme(12, 0, 0), Vrijeme(10, 0, 0))
        self.assertEqual(Vrijeme(12, 0, 0), Vrijeme(12, 0, 0))

    def test_oduzimanje(self):
        self.assertEqual(Vrijeme(10, 10, 10),
                         Vrijeme(20, 10, 10) - Vrijeme(10, 0, 0))
        self.assertEqual(Vrijeme(9, 50, 10),
                         Vrijeme(20, 10, 10) - Vrijeme(10, 20, 0))

    def test_oduzimanje_krivi_argumenti(self):
        with self.assertRaises(TypeError):
            Vrijeme(1, 1, 1) < 'sarma'
        with self.assertRaises(ValueError):
            Vrijeme(1, 1, 62) - Vrijeme(10, 1, 62)


class TestEmisija(unittest.TestCase):
    def test_repr(self):
        e = Emisija("dnevnik", Vrijeme(19, 0, 0), Vrijeme(19, 30, 0))
        self.assertEqual(repr(e), "[dnevnik][19:00:00][19:30:00]")

    def test_krivi_argumenti(self):
        with self.assertRaises(TypeError):
            Emisija("dnevik", 17, 18)

    def test_usporedbe(self):
        e1 = Emisija("dnevnik", Vrijeme(17, 0, 0), Vrijeme(18, 0, 0))
        e2 = Emisija("rambo", Vrijeme(20, 30, 0), Vrijeme(22, 35, 17))
        self.assertLess(e1, e2)
        self.assertGreater(e2, e1)
        self.assertNotEqual(e1, e2)
        self.assertEqual(e1, e1)

    def test_usoredbe_krivi_argument(self):
        with self.assertRaises(TypeError):
            Emisija("dnevik", 17, 18) < 'sarma'


if __name__ == '__main__':
    unittest.main()
