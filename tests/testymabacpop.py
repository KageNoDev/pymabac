import unittest
import numpy as np
from mabac_model import MABAC

class TestMABAC(unittest.TestCase):

#test1
    def test_output1(self):
        """ Test output method with reference:
            Isik, O., Aydin, Y., & Kosaroglu, S. M. (2020). The assessment of the logistics performance index
            of CEE countries with the new combination of SV
            and MABAC methods. LogForum, 16(4), 549-559.
            """
        matrix = np.array([
            [2.937588, 2.762986, 3.233723, 2.881315, 3.015289, 3.313491],  # Bulgaria
            [2.978555, 3.012820, 2.929487, 3.096154, 3.012820, 3.593939],  # Croatia
            [3.286673, 3.464600, 3.746009, 3.715632, 3.703427, 4.133620],  # Czech Republic
            [3.322037, 3.098638, 3.262154, 3.147851, 3.206675, 3.798684],  # Estonia
            [3.354866, 3.270945, 3.221880, 3.213207, 3.670508, 3.785941],  # Hungary
            [2.796570, 2.983000, 2.744904, 2.692550, 2.787563, 2.878851],  # Latvia
            [2.846491, 2.729618, 2.789990, 2.955624, 3.123323, 3.646595],  # Lithuania
            [3.253458, 3.208902, 3.678499, 3.580044, 3.505663, 3.954262],  # Poland
            [2.580718, 2.906903, 3.176497, 3.073653, 3.264727, 3.681887],  # Romania
            [2.789011, 3.000000, 3.101099, 3.139194, 2.985348, 3.139194],  # Slovak Republic
            [3.418681, 3.261905, 3.187912, 3.052381, 3.266667, 3.695238],  # Slovenia
        ])

        weights = np.array([0.171761, 0.105975, 0.191793, 0.168824, 0.161768, 0.199880])
        types = np.array([1, 1, 1, 1, 1, 1])

        output = [8,7,1,5,3,11,10,2,6,9,4]
        mabac = MABAC(matrix, weights, types)
        result = [int(val) for val in mabac.run()]
        self.assertListEqual([max(output) + 1 - r for r in output], result)
        #self.assertListEqual(output, result)

#test2 brak jawnych wag, wzór w artykule omega=v/1+r
    def test_output2(self):
        """ Test output method with reference:
            Đoković, L., & Doljanica, D. (2023). Application of AHP and
            MABAC methods in the framework of multi-criteria decision-making
            in the selection of investment projects. Journal of
            process management and new technologies, 11(3-4), 105-114.
            """
        matrix = np.array([
            [25, 20, 18, 120000, 210000, 2, 3, 8, 6],
            [19, 15, 13, 54000, 66000, 4, 7, 2, 7],
            [23, 16, 12, 30000, 49000, 5, 2, 9, 2],
            [16, 13, 10, 108000, 120000, 1, 8, 1, 9],
            [11, 9, 7, 40000, 98000, 3, 1, 5, 4]
        ])
        weights = np.array([0.25, 0.20, 0.16, 0.12, 0.08, 0.06, 0.05, 0.05, 0.03]) #????
        types = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1])

        #output = [-0.36, -0.11, -0.18, 0.03, 0.10]
        output = [5,3,4,2,1]
        mabac = MABAC(matrix, weights, types)
        result = [int(val) for val in mabac.run()]
        #self.assertListEqual(output, result)
        self.assertListEqual([max(output) + 1 - r for r in output], result)

#test3
    def test_output3(self):
        """ Test output method with reference:
            Yudhana, A., Umar, R., & Fawait, A. B. (2022). Decision Making
            Using the MABAC Method to Determine the Leading Small and
            Medium Industry Centers in Yogyakarta. Ingenierie des
            Systemes d'Information, 27(6), 887.
            """
        matrix = np.array([
            [6, 6045, 55000, 54000, 36000],
            [7, 22680, 15000, 596000, 56000],
            [3, 12000, 40000, 201600, 138000],
            [5, 2880, 2000, 64800, 50400],
            [11, 4500, 5000, 289102, 156702],
            [9, 360, 800000, 350400, 198000],
            [5, 1560, 5000, 93985, 91560],
            [4, 22680, 15000, 596000, 56000],
            [20, 60000, 500000, 174000, 600000],
            [10, 1920, 98150, 216000, 72000],
        ])
        weights = np.array([0.0682, 0.1324, 0.5374, 0.0501, 0.2119])
        types = np.array([1, 1, 1, 1, 0])
        #output = [-0.0366, 0.0200, -0.0702, -0.0878, -0.0773, 0.4310, -0.1014, 0.0079, 0.2382, 0.0008]
        output = [6,3,7,9,8,1,10,4,2,5]

        mabac = MABAC(matrix, weights, types)
        result = [int(val) for val in mabac.run()]
        #self.assertListEqual(output, result)
        self.assertListEqual([max(output) + 1 - r for r in output], result)

#--------------------------------------------------test4
    # def test_output4(self):
    #     """ Test output method with reference:
    #         Wang, J., Darwis, D., Setiawansyah, S., & Rahmanto, Y. (2024).
    #         Implementation of MABAC Method and Entropy Weighting in
    #         Determining the Best E-Commerce Platform for Online Business
    #         JiTEKH, 12(2), 58-68.
    #         """
    #     matrix = np.array([
    #         [9, 6, 8, 7, 8],
    #         [8, 7, 9, 8, 7],
    #         [7, 8, 7, 6, 9],
    #         [8, 6, 9, 9, 8],
    #         [7, 9, 8, 7, 7],
    #         [6, 7, 6, 9, 6],
    #     ])
    #     weights = np.array([0.1732, 0.2302, 0.2018, 0.2216, 0.1732])
    #     types = np.array([1, 1, 1, 1, 1])
    #     #output = [-0.0682, 0.0035, -0.0927, 0.1767, 0.1089, 0.1143]
    #     output = [5,4,6,1,3,2]
    #
    #     mabac = MABAC(matrix, weights, types)
    #     result = [int(val) for val in mabac.run()]
    #     #self.assertListEqual(output, result)
    #     self.assertListEqual([max(output) + 1 - r for r in output], result)

#test 5
    def test_output5(self):
        """ Test output method with reference:
            Vesković, S., Stević, Ž., Stojić, G., Vasiljević, M., & Milinković, S.
            (2018). Evaluation of the railway management model by using a
            new integrated model DELPHI-SWARA-MABAC. Decision
            Making: Applications in Management and Engineering, 1(2), 34-50.
            """
        matrix = np.array([
            [4.238, 3.918, 4.530, 3.710, 4.502, 4.810],
            [5.142, 4.786, 4.698, 5.433, 5.174, 6.706],
            [6.470, 4.909, 5.463, 6.069, 6.020, 6.392],
            [4.341, 7.471, 4.900, 7.796, 5.051, 3.580],
        ])
        weights = np.array([0.203, 0.150, 0.224, 0.129, 0.177, 0.117])
        types = np.array([1, 1, 1, 1, 1, 1])
        #output = [-0.334, 0.029, 0.398, 0.100]
        output = [4,3,1,2]

        mabac = MABAC(matrix, weights, types)
        result = [int(val) for val in mabac.run()]
        #self.assertListEqual(output, result)
        self.assertListEqual([max(output) + 1 - r for r in output], result)

#test 6
    # def test_output6(self):
    #     """ Test output method with reference:
    #         Hristov, N., Pamucar, D., & Amine, M. S. M. E. (2021).
    #         Application of a D number based LBWA model and an interval
    #         MABAC model in selection of an automatic cannon for
    #         integration into combat vehicles. Defence Science Journal,
    #         71(1), 34.
    #         """
    #     matrix = np.array([
    #         [0.607, 0.798, 0.000, 0.519, 0.333, 0.667, 0.579],
    #         [0.796, 0.547, 0.438, 0.556, 0.667, 0.667, 0.602],
    #         [0.000, 0.998, 0.313, 0.000, 0.000, 0.000, 0.877],
    #         [0.313, 1.000, 0.750, 0.426, 0.000, 0.333, 1.000],
    #         [0.596, 0.766, 0.250, 1.000, 0.333, 0.000, 0.731],
    #         [0.472, 0.776, 1.000, 0.426, 0.000, 0.333, 0.836],
    #         [0.792, 0.338, 0.000, 0.481, 0.667, 1.000, 0.339],
    #         [1.000, 0.000, 0.000, 0.352, 1.000, 1.000, 0.000],
    #         [0.243, 0.529, 0.625, 0.056, 0.000, 0.000, 0.994],
    #     ])
    #     weights = np.array([0.0752, 0.0771, 0.1132, 0.1159, 0.2225, 0.2428, 0.1533])
    #     #w = [(w− + w+)/2 wagi usrednione
    #     types = np.array([1, 0, 1, 1, 1, 1, 0])
    #     #output = [0.080, 0.233, -0.208, 0.067, 0.014, 0.047, 0.178, 0.149, -0.156]
    #     output = [4,1,9,5,7,6,2,3,8]
    #
    #     mabac = MABAC(matrix, weights, types)
    #     result = [int(val) for val in mabac.run()]
    #     #self.assertListEqual(output, result)
    #     self.assertListEqual([max(output) + 1 - r for r in output], result)

#test7
    def test_output7(self):
        """ Test output method with reference:
            Setiawansyah, S., Hadad, S. H., Aldino, A. A., Palupiningsih, P.,
            Laxmi, G. F., & Megawaty, D. A. (2024). Employing PIPRECIA-S
            weighting with MABAC: a strategy for identifying organizational
            leadership elections. Bulletin of Electrical Engineering and
            Informatics, 13(6), 4273-4284.
            """
        matrix = np.array([
            [80, 85, 89, 79, 90, 87],
            [78, 83, 87, 78, 80, 85],
            [81, 85, 89, 80, 86, 87],
            [79, 84, 88, 79, 84, 86],
            [81, 86, 90, 81, 91, 88],
            [82, 86, 90, 81, 88, 88],
        ])
        weights = np.array([0.196, 0.164, 0.164, 0.196, 0.140, 0.140])
        types = np.array([1, 0, 1, 1, 1, 1])
        #output = [0.042, -0.340, 0.107, -0.129, 0.283, 0.293]
        output = [4,6,3,5,2,1]

        mabac = MABAC(matrix, weights, types)
        result = [int(val) for val in mabac.run()]
        #self.assertListEqual(output, result)
        self.assertListEqual([max(output) + 1 - r for r in output], result)

#test 8
    def test_output8(self):
        """ Test output method with reference:
            Nunić, Z. (2018). Evaluation and selection of the PVC carpentry
            manufacturer using the FUCOM-MABAC model. Operational
            Research in Engineering Sciences: Theory and Applications,
            1(1), 13-28.
            """
        matrix = np.array([
            [7, 5776.000, 5, 5, 5, 3, 5],
            [7, 8252.780, 2, 3, 5, 3, 1],
            [7, 3490.030, 5, 5, 5, 3, 7],
            [3, 4355.000, 5, 3, 3, 3, 1],
            [5, 5795.000, 0, 3, 1, 1, 1],
        ])
        weights = np.array([0.266, 0.207, 0.108, 0.098, 0.134, 0.108, 0.079])
        types = np.array([1, 0, 1, 1, 1, 1, 1])
        #output = [0.307, -0.016, 0.433, -0.115, -0.327]
        output = [2,3,1,4,5]

        mabac = MABAC(matrix, weights, types)
        result = [int(val) for val in mabac.run()]
        #self.assertListEqual(output, result)
        self.assertListEqual([max(output) + 1 - r for r in output], result)

#test9
    # def test_output9(self):
    #     """ Test output method with reference:
    #         Muravev, D., & Mijic, N. (2020). A novel integrated provider
    #         selection multicriteria model: The BWM-MABAC model. Decision
    #         Making: Applications in Management and Engineering, 3(1), 60-78.
    #         """
    #     matrix = np.array([
    #         [65, 23, 56, 53, 54, 95, 53, 59, 62], #brak S1 dla a1???
    #         [45, 29, 50, 49, 49, 87, 63, 73, 44],
    #         [56, 43, 70, 57, 59, 52, 59, 41, 41],
    #         [70, 35, 82, 43, 91, 93, 38, 66, 41],
    #         [82, 68, 63, 95, 35, 81, 79, 39, 49],
    #         [90, 56, 71, 80, 62, 71, 91, 23, 81],
    #         [48, 39, 63, 74, 25, 66, 66, 72, 52],
    #         [76, 56, 59, 61, 53, 77, 59, 46, 77],
    #     ])
    #     weights = np.array([0.1395, 0.1640, 0.1982, 0.1040, 0.0687, 0.0842, 0.0740, 0.1095,0.0505])
    #     types = np.array([1, 1, 1, 1, 0, 1, 1, 0, 1])
    #     #output = [-0.104, 0.007, 0.120, 0.137, 0.212, -0.018, 0.025] #nie ma s1
    #     output = [8,7,4,6,2,1,3,5]
    #     mabac = MABAC(matrix, weights, types)
    #     result = [int(val) for val in mabac.run()]
    #     #self.assertListEqual(output, result)
    #     self.assertListEqual([max(output) + 1 - r for r in output], result)

#test10
    def test_output10(self):
        """ Test output method with reference:
            Singh, T., Pattnaik, P., Aherwar, A., Ranakoti, L., Dogossy, G., &
            Lendvai, L. (2022). Optimal design of wood/rice husk-waste-filled
            PLA biocomposites using integrated CRITIC–MABAC-based
            decision-making algorithm. Polymers, 14(13), 2603.
            """
        matrix = np.array([
            [57.96, 105.67, 15.25, 99.53, 2.56, 2.71, 3.43, 1.240, 0.36, 0.1652],
            [51.13, 101.40, 11.42, 99.67, 2.77, 3.25, 3.58, 1.263, 0.78, 0.1142],
            [51.19, 100.84, 11.25, 99.33, 2.79, 3.36, 3.69, 1.266, 1.16, 0.1014],
            [50.06, 102.12,  8.75, 97.84, 2.89, 3.45, 3.92, 1.272, 1.44, 0.1644],
            [50.23, 101.86,  9.63, 97.36, 3.02, 3.58, 4.03, 1.277, 1.74, 0.2047],
            [53.01,  99.44, 12.31, 100.20, 2.66, 2.94, 3.51, 1.225, 0.94, 0.1176],
            [51.87, 100.86, 10.44, 100.43, 2.78, 3.36, 3.74, 1.211, 1.56, 0.1646],
            [51.52, 100.68,  9.38, 99.96, 2.94, 3.43, 3.90, 1.198, 1.90, 0.2017],
            [50.90,  99.98,  9.63, 99.01, 2.97, 3.46, 4.03, 1.183, 1.92, 0.2618],
        ])
        weights = np.array([0.0802, 0.0810, 0.0822, 0.0951, 0.1148, 0.1136, 0.1306, 0.1092, 0.0963, 0.0970])
        types = np.array([1, 1, 1, 1, 1, 1, 1, 0, 0, 0])
        #output = [0.0588, 0.1151, 0.1303, -0.0218, -0.0041, 0.1464, 0.0687, 0.0898, 0.0674]
        output = [4,6,5,9,7,8,2,1,3]

        mabac = MABAC(matrix, weights, types)
        result = [int(val) for val in mabac.run()]
        #self.assertListEqual(output, result)
        self.assertListEqual([max(output) + 1 - r for r in output], result)

#test11
    def test_output11(self):
        """ Test output method with reference:
            Lukic, R. (2021). Analysis of trade efficiency in Serbia based on
            the MABAC method. Economic outlook, 23(2), 1-18.
            """
        matrix = np.array([
            [193210, 151978, 2160474, 746992, 2891518, 89730],
            [191621, 154833, 2157564, 761305, 2594602, 86955],
            [159621, 164718, 2197931, 805009, 2731999, 95265],
            [206092, 180367, 2324843, 859749, 3009651, 105238],
            [208020, 194924, 2375290, 920992, 3172393, 122727],
            [219373, 218410, 2524897, 1007972, 3361094, 121816],
            [222049, 238022, 2682931, 1073056, 3608329, 139409],
            [227618, 262322, 2837599, 1183026, 3664505, 171010],
        ])
        weights = np.array([0.2267, 0.2020, 0.1545, 0.1394, 0.1426, 0.1347])
        types = np.array([0, 0, 1, 1, 1, 1])
        #output = [-0.0343, -0.0744, 0.0690, -0.0153, 0.0324, 0.0371, 0.1101, 0.1755]
        output = [7,8,3,6,5,4,2,1]

        mabac = MABAC(matrix, weights, types)
        result = [int(val) for val in mabac.run()]
        #self.assertListEqual(output, result)
        self.assertListEqual([max(output) + 1 - r for r in output], result)

#test12
    def test_output12(self):
        """ Test output method with reference:
            Sihombing, D. O., & Cahyadi, A. (2023). Implementasi Metode
            MABAC Dalam Pemilihan Mahasiswa Terbaik dengan Teknik
            Pembobotan Rank Sum. J. Comput. Syst. Informatics, 4(4),
            1008-1018.
            """
        matrix = np.array([
            [4.00, 10.00, 1, 100.00, 3],
            [3.98, 16.50, 1, 95.83, 3],
            [2.80, 2.50, 1, 83.33, 3],
            [2.28, 2.00, 1, 70.83, 3],
            [4.00, 5.00, 1, 100.00, 3],
            [3.96, 11.00, 1, 95.83, 3],
            [2.79, 3.50, 1, 87.50, 3],
            [2.38, 1.00, 1, 62.50, 2],
            [4.00, 4.00, 1, 87.50, 3],
            [3.98, 10.50, 1, 100.00, 2],
            [3.02, 2.00, 2, 45.83, 3],
            [2.91, 2.50, 1, 95.83, 3],
        ])
        weights = np.array([0.3333, 0.2667, 0.2000, 0.1333, 0.0667])
        types = np.array([1, 1, 0, 1, 1])
        output = [0.300363, 0.398068, -0.102242, -0.242370, 0.214330, 0.299556, -0.076712, -0.327397, 0.166364, 0.238390, -0.360493, -0.050166]
        output = [2,1,9,10,5,3,8,11,6,4,12,7]
        mabac = MABAC(matrix, weights, types)
        result = [int(val) for val in mabac.run()]
        #self.assertListEqual(output, result)
        self.assertListEqual([max(output) + 1 - r for r in output], result)

#test13
    def test_output13(self):
        """ Test output method with reference:
            Wang, J., Wen, J., Pajić, V., & Andrejić, M. (2024). Optimizing
            cross-dock terminal location selection: A multi-step approach
            based on CI-DEA–IDOCRIW–MABAC for enhanced supply
            chain efficiency—A case study. Mathematics, 12(5), 736.
            """
        matrix = np.array([
            [3, 4, 2, 6, 3, 2, 4, 2, 4],
            [3, 2, 3, 3, 4, 3, 5, 3, 5],
            [5, 5, 4, 4, 7, 7, 7, 4, 4],
            [4, 3, 5, 6,10, 9, 6, 5, 3],
        ])
        weights = np.array([0.0340, 0.1266, 0.0643, 0.0401, 0.2059, 0.3005, 0.0763, 0.1358, 0.0163])
        types = np.array([0, 1, 0, 0, 1, 1, 1, 1, 0])
        #output = [-0.2319, -0.1627, 0.2594, 0.3459]
        output = [4,3,2,1]

        mabac = MABAC(matrix, weights, types)
        result = [int(val) for val in mabac.run()]
        #self.assertListEqual(output, result)
        self.assertListEqual([max(output) + 1 - r for r in output], result)
