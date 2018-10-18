from .File import File
import pandas as pd

from .wetb.hawc2.ae_file import AEFile

class HAWC2AEFile(File):

    @staticmethod
    def defaultExtensions():
        return ['.dat','.ae','.txt']

    @staticmethod
    def formatName():
        return 'HAWC2 AE file (.dat, .ae, .txt)'

    def _read(self):
        self.data = AEFile(self.filename)
        #self.data = pd.read_csv(self.filename,sep=self.sep)
        #self.data.rename(columns=lambda x: x.strip(),inplace=True)

    #def _write(self):
        #self.data.to_csv(self.filename,sep=self.false,index=False)

    def _toDataFrame(self):
        cols=['radius_[m]','chord_[m]','thickness_[%]','pc_set_[#]']
        nset = len(self.data.ae_sets)
        if nset == 1:
            return pd.DataFrame(data=self.data.ae_sets[1], columns=cols)
        else:
            dfs = {}
            for iset,aeset in enumerate(self.data.ae_sets):
                name='ae_set_{}'.format(iset+1)
                dfs[name] = pd.DataFrame(data=self.data.ae_sets[iset+1], columns=cols)
            return dfs

