#include ....

void main() {
  TFile *f = TFile::Open("test.root");
  TTree *tree = (TTree*)f->Get("DecayTree");
  TCanvas *c1 = new TCanvas("c1","c1");
  
  int bins = 100;
  double min = 5000.;
  double max = 7000.;
  TH1D *histo = new TH1D("dummy histogram", "dummy", bins, min, max);
  
  double Xibm_E, Xibm_PT, ...;
  
  tree->SetBranchAddress("Xibm_E", &Xibm_E),
  tree->SetBranchAddress("Xibm_PT", &Xibm_PT),
  ...
  double treesize = tree->GetEntries();
  for(int i=0; i<treesize; i++) {
    tree->GetEntry();
    histo->Fill(Xibm_E);
  }
  histo->Draw();
}