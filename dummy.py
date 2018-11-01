#!/bash/bin/python

c_str = """#include ....

void main() {
  TFile *f = TFile::Open("test.root");
  TTree *tree = (TTree*)f->Get("DecayTree");
  TCanvas *c1 = new TCanvas("c1","c1");
  
  int bins = 100;
  double min = 5000.;
  double max = 7000.;
  TH1D *histo = new TH1D("dummy histogram", "dummy", bins, min, max);
  double 
  """
vars = ['Xibm_E', 'Xibm_PT']

for var in vars:
	c_str += var

c_str += ';\n'

for var in vars:
	c_str += 'tree->SetBranchAddress("%s", &%s);\n'%(var, var)
	
c_str += '''...
  double treesize = tree->GetEntries();
  for(int i=0; i<treesize; i++) {
    tree->GetEntry();
    histo->Fill(Xibm_E);
  }
  histo->Draw();
}'''

f = open('test.c','w')
f.writeline(c_str)
f.close()