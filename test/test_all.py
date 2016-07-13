import sys, unittest

# attempt to use the most current library
sys.path.insert(0, '..')
from statlib import stats, pstat

try:
    from numpy import array as num_array
except ImportError:
    # numpy not installed
    sys.stderr.write('Numpy not installed ... skipping numpy tests\n')
    # falls back to lists
    def num_array( values ):
        return values

class TestStatlib(unittest.TestCase):
    
    def setUp(self):
        "Gets called on each test"
        # generate list data
        self.L  = self.LF = range( 1, 21 )
        self.LF[2] = 3.0
        self.LL = [ self.L ] * 5

        # array data if numpy is installed
        self.A  = self.AF = num_array( self.L )
        self.AA = num_array( self.LL )
        
        self.M = range(4,24)
        self.M[10] = 34 
        self.B = num_array(self.M)
        
        self.PB = [0]*9 + [1]*11
        self.APB = num_array(self.PB)
        
        self.EQ = self.assertAlmostEqual

    def test_geometricmean(self):
        "Testing geometric mean"
        data = [ self.L, self.LF, self.A, self.AF  ]
        for d in data :
            self.EQ( stats.geometricmean( d ), 8.304, 3)

    def test_harmonicmean(self):
        "Testing harmonic mean"
        data = [ self.L, self.LF, self.A, self.AF  ]
        for d in data :
            self.EQ( stats.harmonicmean( d ), 5.559, 3)

    def test_mean(self):
        "Testing mean"
        data = [ self.L, self.LF, self.A, self.AF  ]
        for d in data :
            self.EQ( stats.mean( d ), 10.5, 3)

    def test_median(self):
        "Testing median"
        data = [ self.L, self.LF, self.A, self.AF  ]
        for d in data :
            self.assertTrue( 10 < stats.median( d ) < 11 )
    
    def test_medianscore(self):
        "Testing medianscore"
        
        # data of even lenghts
        data1 = [ self.L, self.LF, self.A, self.AF  ]
        for d in data1 :
            self.EQ( stats.medianscore( d ), 10.5 )

        # data with odd lenghts
        L2 = self.L + [ 20 ]
        A2 = num_array( L2 )
        data2 = [ L2, A2  ]
        for d in data2:
            self.EQ( stats.medianscore( d ), 11 )

 
    def test_mode(self):
        "Testing mode"
        L1 = [1,1,1,2,3,4,5 ]
        L2 = [1,1,1,2,3,4,5,6 ]

        A1 = num_array( L1 )
        A2 = num_array( L2 )
        data = [ L1, L2, A1, A2  ]
        for d in data :
            self.assertEqual( stats.mode( d ), (3, [1]) )

    # Moments
    
    def test_moment(self):
        "Testing moment"
        data = [ self.L, self.LF, self.A, self.AF ]
        for d in data:
            self.assertEqual( stats.moment( d ), 0.0 )
    
    def test_variation(self):
        "Testing variation"
        data = [ self.L, self.A, self.LF, self.AF ]
        for d in data:
            self.EQ( stats.variation( d ), 54.9169647365 )

    def test_skew(self):
        "Testing skew"
        data = [ self.L, self.LF, self.A, self.AF ]
        for d in data:
            self.assertEqual( stats.skew( d ), 0.0 )

    def test_kurtosis(self):
        "Testing kurtosis"
        data  = [ self.L, self.LF, self.A, self.AF ]
        for d in data:
            self.EQ( stats.kurtosis( d ), 1.79398496241 )
    
    def test_tmean(self):
        "Testing tmean"
        data = [ self.A, self.AF ]
        for d in data:
            self.assertEqual( stats.tmean( d, ( 5, 17 ) ), 11.0 )
    
    def test_tvar(self):
        "Testing tvar"
        data = [ self.A, self.AF ]
        for d in data:
            self.EQ( stats.tvar( d, ( 5, 17 ) ), 15.1666666667 )
            
    def test_tstdev(self):
        "Testing tstdev"
        data = [ self.A, self.AF ]
        for d in data:
            self.EQ( stats.tstdev( d, ( 5, 17 ) ), 3.89444048185 )
            
    def test_tsem(self):
        "Testing tsem"
        data = [ self.A, self.AF ]
        for d in data:
            self.EQ( stats.tsem( d, ( 5, 17 ) ), 1.08012344973 )
    
    def test_describe(self):
        "Testing describe"
        self.assertEqual( stats.describe( self.L ), (20, (1, 20), 10.5, 5.9160797830996161, 0.0, 1.7939849624060149) )
        self.assertEqual( stats.describe( self.LF ), (20, (1, 20), 10.5, 5.9160797830996161, 0.0, 1.7939849624060149) )    
        self.assertEqual( stats.describe( self.A ), (20, (1, 20), 10.5, 5.9160797830996161, num_array(0.0), num_array(1.7939849624060149)) )
        self.assertEqual( stats.describe( self.AF ), (20, (1, 20), 10.5, 5.9160797830996161, num_array(0.0), num_array(1.7939849624060149)) )
    
    # frequency
    
    def test_itemfreq(self):
        "Testing itemfreq"
        self.assertEqual( stats.itemfreq( self.L ), [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1], [16, 1], [17, 1], [18, 1], [19, 1], [20, 1]] )
       # self.assertEqual( stats.itemfreq( self.A ), num_array([[  1.,   1.],[  2.,   1.],[  3.,   1.],[  4.,   1.],[  5.,   1.],[  6.,   1.],[  7.,   1.],[  8.,   1.],[  9.,   1.],[ 10.,   1.],[ 11.,   1.],[ 12.,   1.],[ 13.,   1.],[ 14.,   1.],[ 15.,   1.],[ 16.,   1.],[ 17.,   1.],[ 18.,   1.],[ 19.,   1.],[ 20.,   1.]]))
        
    
    def test_scoreatpercentile(self):
        "Testing scoreatpercentile"
        data = [ self.L, self.LF, self.A, self.AF ]
        for d in data:
            self.EQ( stats.scoreatpercentile( d, 40 ), 8.31500035 ) 
    
    def test_percentileofscore(self):
        "Testing percentileofscore"
        data = [ self.L, self.LF, self.A, self.AF ]
        for d in data:
            self.EQ( stats.percentileofscore( d, 12 ), 57.6315764291 )
    
    def test_histogram(self):
        "Testing histogram"
        data = [ self.L, self.A ]
        results1 = ([2, 2, 2, 2, 2, 2, 2, 2, 2, 2], -0.045000050000000069, 2.0900001000000001, 0)
        results2 = (num_array([ 2.,  2.,  2.,  2.,  2.,  2.,  2.,  2.,  2.,  2.]), -0.045000050000000069, 2.0900001000000001, 0)
        
        i = 0
        for d in data:
            self.assertEqual( stats.histogram( d )[i], results1[i] ) 
            i += 1
        # hmm...
    def test_cumfreq(self):
        "Testing cumfreq"
        data = [ self.L, self.LF, self.A, self.AF ]
        results1 = ([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], -0.045000050000000069, 2.0900001000000001, 0 )
        results2 = ([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], -0.045000050000000069, 2.0900001000000001, 0 )
        results3 = (num_array([  2.,   4.,   6.,   8.,  10.,  12.,  14.,  16.,  18.,  20.]), -0.045000050000000069, 2.0900001000000001, 0 )
        results4 = (num_array([  2.,   4.,   6.,   8.,  10.,  12.,  14.,  16.,  18.,  20.]), -0.045000050000000069, 2.0900001000000001, 0 )
        
        i = 0
        for d in data:
            self.assertEqual( stats.cumfreq( d )[i], results1[i] )
            i += 1
            
        #hmm...    
    def test_relfreq(self):
        "Testing relfreq"
        
        data = [ self.L, self.LF, self.A, self.AF ]
        results1 = ([0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001], -0.045000050000000069, 2.0900001000000001, 0)
        results2 = ([0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001, 0.10000000000000001], -0.045000050000000069, 2.0900001000000001, 0)
        results3 = (num_array([ 0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1]), -0.045000050000000069, 2.0900001000000001, 0)
        results4 = (num_array([ 0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1,  0.1]), -0.045000050000000069, 2.0900001000000001, 0)
        
        i = 0
        for d in data:
            self.assertEqual( stats.relfreq( d )[i], results1[i])
            i += 1
    
    # variation    
    def test_obrientransform(self):
        "Testing obrientransform"
        results = [ 96.66666667,  77.19298246,  59.88304094,  44.73684211,  31.75438596,
                    20.93567251,  12.28070175,   5.78947368,   1.4619883,   -0.70175439,
                    -0.70175439,   1.4619883,    5.78947368,  12.28070175,  20.93567251,
                    31.75438596,  44.73684211,  59.88304094,  77.19298246,  96.66666667]
 

        i = 0
        for f in results: # we'll look at the first results only
           self.EQ( stats.obrientransform( self.L, self.L, self.L, self.L, self.L)[0][i], f )
           i += 1
       
    
    def test_samplevar(self):
        "Testing samplevar"
        
        data = [ self.L, self.A ]
        
        for d in data:
            self.assertEqual( stats.samplevar( d ), 33.25 )
    
    def test_samplestdev(self):
        "Testing samplestdev"
        
        data = [ self.L, self.A ]
        for d in data:
            self.EQ( stats.samplestdev( d ), 5.76628129734 )
    
    def test_var(self):
        "Testing var"
        
        data = [ self.L, self.A ]
        for d in data:
            self.EQ( stats.var( d ), 35.0 )
    
    def test_stdev(self):
        "Testing stdev"
        
        data = [ self.L, self.A ]
        for d in data:
            self.EQ( stats.stdev( d ), 5.9160797831 )
            
    def test_sterr(self):
        "Testing sterr"
        
        data = [ self.L, self.A ]
        for d in data:
            self.EQ( stats.sterr( d ), 1.32287565553 )        
    
    def test_sem(self):
        "Testing sem"
        
        data = [ self.L, self.A ]
        for d in data:
            self.EQ( stats.sem( d ), 1.32287565553 )        
        
    def test_z(self):
        "Testing z"
        
        data = [ self.L, self.A ]
        for d in data:
            self.EQ( stats.z( d, 4 ), -1.12724296038)
    # Trimming
    
    def test_trimboth(self):
        "Testing trimboth"
        
        data = [ self.L, self.LF, self.A, self.AF ]
        results = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        i = 0 
        for d in data:
            self.assertEqual( stats.trimboth( d, .2 )[i], results[i])
            i += 1
        # hmm...
    
    def test_trim1(self):
        "Testing trim1"
        
        data = [ self.L, self.LF, self.A, self.AF ]
        results = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        i = 0 
        for d in data:
            self.assertEqual( stats.trim1( d, .2 )[i], results[i])
            i += 1
        # hmm...    
    
    # Correlation
    def test_pearsonr(self):
        "Testing pearsonr"
        
        data1 = [ self.L, self.A ]
        data2 = [ self.M, self.B ]
        results = (0.80208084775070976, 2.1040104471429959e-005)
        
        i = 0
        for d in data1:
           self.assertEqual( stats.pearsonr( d, data2[i] )[i], results[i] )
           i += 1
    
    def test_spearmanr(self):
        "Testing spearmanr"
        
        data1 = [ self.L, self.A ]
        data2 = [ self.M, self.B ]
        results = (0.93233082706766912, 2.2066972068439387e-009)
        
        i = 0
        for d in data1:
           self.assertEqual( stats.spearmanr( d, data2[i] )[i], results[i] )
           i += 1
    
    def test_pointbiserialr(self):
        "Testing pointbiserialr"
        
        data1 = [ self.PB, self.APB ]
        data2 = [ self.L, self.A ]
        results = (0.8627635262664034, 9.8591235557031489e-007)
        
        i = 0
        for d in data1:
          self.assertEquals( stats.pointbiserialr( d, data2[i] )[i], results[i] )
          i += 1
        
    def test_kendalltau(self):
        "Testing kendalltau"
        
        data1 = [ self.L, self.A ]
        data2 = [ self.M, self.B ]
        results = (0.86313455447495724, 1.0335817091423592e-007)
        
        i = 0
        for d in data1:
           self.assertEqual( stats.kendalltau( d, data2[i] )[i], results[i] )
           i += 1
           
    def test_linregress(self):
        "Testing linregress"
        
        data1 = [ self.L, self.A ]
        data2 = [ self.M, self.B ]
        results = (1.0150375939849625, 3.8421052631578938, 0.80208084775070976, 2.1040104471429959e-005, 4.3580363930338537)
    
        i = 0
        for d in data1: # so check the first two of results...
           self.assertEqual( stats.linregress( d, data2[i] )[i], results[i] )
           i += 1
           
    # Inferential
    
    def test_ttest_1samp(self):
        "Testing ttest_1samp"
        
        data = [ self.L, self.A ]
        results = (-1.1338934190276817, 0.27094394816451473)
        
        i = 0
        for d in data:
            self.assertEqual( stats.ttest_1samp( d, 12 )[i], results[i] )
            i += 1
    results = (-1.1338934190276817, 0.27094394816451473)
    
    
    def test_ttest_ind(self):
        "Testing ttest_ind"
        
        data1 = [ self.L, self.A ]
        data2 = [ self.M, self.B ]
        results = (-1.8746868717340566, 0.068537696711420654)
        
        i = 0
        for d in data1:
            self.assertEqual( stats.ttest_ind( d, data2[i] )[i], results[i] )
            i += 1
    
    def test_ttest_rel(self):
        "Testing ttest_rel"
        
        data1 = [ self.L, self.A ]
        data2 = [ self.M, self.B ]
        results = (-4.0, 0.00076619233678407726)
        
        i = 0
        for d in data1:
            self.assertEqual( stats.ttest_rel( d, data2[i] )[i], results[i] )
            i += 1
    
    def test_chisquare(self):
        "Testing chisquare"
        
        data = [ self.L, self.A ]
        
        results = (63.333333333333329, 1.1339262036309899e-006)
        
        i = 0
        for d in data:
            self.EQ( stats.chisquare( d )[i], results[i] )
            i += 1
    
    def test_ks_2samp(self):
        "Testing ks_2samp"
        
        data1 = [ self.L, self.A ]
        data2 = [ self.M, self.B ]
        results = (-0.20000000000000007, 0.77095294467662123)
        
        i = 0
        for d in data1:
            self.assertEqual( stats.ks_2samp( d, data2[i] )[i], results[i] )
            i += 1
    
    def test_mannwhitneyu(self):
        "Testing mannwhitneyu"
        
        data1 = [ self.L, self.A ]
        data2 = [ self.M, self.B ]
        results = (138.0, 0.046699380915068867)    
        
        i = 0
        for d in data1:
            self.assertEqual( stats.mannwhitneyu( d, data2[i] )[i], results[i] )
            i += 1        
    
    def test_ranksums(self):
        "Testing ranksums"
        
        data1 = [ self.L, self.A ]
        data2 = [ self.M, self.B ]
        results = (-1.677105520481424, 0.09352184967262378)
        
        i = 0
        for d in data1:
            self.assertEqual( stats.ranksums( d, data2[i] )[i], results[i] )
            i += 1        
    def test_wilcoxont(self):
        "Testing wilcoxont"
        
        data1 = [ self.L, self.A ]
        data2 = [ self.M, self.B ]
        results = (0.0, 8.8574167624866362e-005)
        
        i = 0
        for d in data1:
            self.assertEqual( stats.wilcoxont( d, data2[i] )[i], results[i] )
            i += 1        
    
    def test_kruskalwallish(self):
        "Testing kruskalwallish"
        
        data1 = [ self.L, self.A ]
        data2 = [ self.M, self.B ]
        data3 = [ self.L, self.A ]
        results = (3.7881409721062096, 0.15045812299265815)
        
        i = 0
        for d in data1:
            self.EQ( stats.kruskalwallish( d, data2[i], data3[i] )[i], results[i] )
            i += 1
            
    def test_friedmanchisquare(self):
        "Testing friedmanchisquare"
        
        data1 = [ self.L, self.A ]
        data2 = [ self.M, self.B ]
        data3 = [ self.L, self.A ]
        results = (8375.0, 0.0)
        
        i = 0
        for d in data1:
            self.EQ( stats.friedmanchisquare( d, data2[i], data3[i] )[i], results[i] )
            i += 1
            
    # ANOVAs
    def test_oneway(self):
        "Testing F_oneway"
        data1 = [ self.L, self.A ]
        data2 = [ self.M, self.B ]
        results = (3.5144508670520231, 0.068537696711420654)
        
        i = 0
        for d in data1:
           self.assertEqual( stats.F_oneway( d, data2[i] )[i], results[i] )
           i += 1
        
        
    # Support
    def test_sum(self):
        "Testing sum"
        
        data = [ self.L, self.LF, self.A, self.AF ]
    
        for d in data:
            self.assertEqual( stats.sum( d ), 210.0 )
    
    def test_cumsum(self):
        "Testing cumsum"
        
        data = [ self.L, self.LF, self.A, self.AF ]
        results = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]
        i = 0 
        for d in data:
            self.assertEqual( stats.cumsum( d )[i], results[i])
            i += 1
        # hmm...
    
    def test_ss(self):
        "Testing ss"
        
        data = [ self.L, self.LF, self.A, self.AF ]
        for d in data:
            self.assertEqual( stats.ss( d ), 2870.0)
      
    def test_summult(self):
        "Testing summult"
        
        data1 = [ self.L, self.LF, self.A, self.AF ]
        data2 = [ self.M, self.M, self.B, self.B ]
        i = 0
        for d in data1:
            self.assertEqual( stats.summult( d, data2[i] ), 3720.0 )
            i += 1
    
    def test_sumsquared(self):
        "Testing square_of_sums"
        
        data = [ self.L, self.LF, self.A, self.AF ]
        for d in data:
            self.assertEqual( stats.square_of_sums( d ), 44100.0 )

    def test_sumdiffsquared(self):
        "Testing sumdiffsquared"
        
        data1 = [ self.L, self.LF, self.A, self.AF ]
        data2 = [ self.M, self.M, self.B, self.B ]
         
        i = 0
        for d in data1:
            self.assertEqual( stats.sumdiffsquared( d, data2[i] ), 700.0 )
            i += 1
            
    def test_shellsort(self):
        "Testing shellsort"
        
        result = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 34]
        
        i = 0
        for f in result: # we'll look at the first results only
           self.EQ( stats.shellsort( self.M )[0][i], f )
           i += 1 
        
    def test_rankdata(self):
        "Testing rankdata"
        
        results = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 20.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0]
        
        data = [ self.M, self.B ]
        
        i = 0
        for d in data:
            self.assertEqual( stats.rankdata( d )[i], results[i])
            i += 1
    
def get_suite():
    suite = unittest.TestLoader().loadTestsFromTestCase( TestStatlib )
    return suite

if __name__ == '__main__':
    suite = get_suite()
    unittest.TextTestRunner(verbosity=2).run(suite)