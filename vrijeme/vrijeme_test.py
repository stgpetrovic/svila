import unittest
import vrijeme


class TestVrijeme(unittest.TestCase):
    def test_repr(self):
        v = vrijeme.Vrijeme(17, 3, 23)
        self.assertEqual(repr(v), "17:03:23")

    def test_krivi_tip_sat(self):
        with self.assertRaises(TypeError):
            vrijeme.Vrijeme('a', 1, 1)

    def test_krivi_tip_minuta(self):
        with self.assertRaises(TypeError):
            vrijeme.Vrijeme(1, 'a', 1)

    def test_krivi_tip_sekunda(self):
        with self.assertRaises(TypeError):
            vrijeme.Vrijeme(1, 1, 'a')

    def test_preveliki_broj_sat(self):
        with self.assertRaises(ValueError):
            vrijeme.Vrijeme(25, 1, 1)

    def test_preveliki_broj_minuta(self):
        with self.assertRaises(ValueError):
            vrijeme.Vrijeme(1, 61, 1)

    def test_preveliki_broj_sekunda(self):
        with self.assertRaises(ValueError):
            vrijeme.Vrijeme(1, 1, 62)

    def test_usporedbe(self):
        self.assertLess(vrijeme.Vrijeme(12, 0, 0), vrijeme.Vrijeme(14, 0, 0))
        self.assertGreater(vrijeme.Vrijeme(12, 0, 0),
                           vrijeme.Vrijeme(10, 0, 0))
        self.assertEqual(vrijeme.Vrijeme(12, 0, 0), vrijeme.Vrijeme(12, 0, 0))

    def test_oduzimanje(self):
        self.assertEqual(
            vrijeme.Vrijeme(10, 10, 10),
            vrijeme.Vrijeme(20, 10, 10) - vrijeme.Vrijeme(10, 0, 0))
        self.assertEqual(
            vrijeme.Vrijeme(9, 50, 10),
            vrijeme.Vrijeme(20, 10, 10) - vrijeme.Vrijeme(10, 20, 0))

    def test_oduzimanje_krivi_argumenti(self):
        with self.assertRaises(TypeError):
            vrijeme.Vrijeme(1, 1, 1) < 'sarma'
        with self.assertRaises(ValueError):
            vrijeme.Vrijeme(1, 1, 62) - vrijeme.Vrijeme(10, 1, 62)


if __name__ == '__main__':
    unittest.main()
