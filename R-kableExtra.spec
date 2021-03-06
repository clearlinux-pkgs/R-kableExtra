#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-kableExtra
Version  : 1.3.4
Release  : 8
URL      : https://cran.r-project.org/src/contrib/kableExtra_1.3.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/kableExtra_1.3.4.tar.gz
Summary  : Construct Complex Table with 'kable' and Pipe Syntax
Group    : Development/Tools
License  : MIT
Requires: R-digest
Requires: R-glue
Requires: R-htmltools
Requires: R-knitr
Requires: R-magrittr
Requires: R-rmarkdown
Requires: R-rstudioapi
Requires: R-rvest
Requires: R-scales
Requires: R-stringr
Requires: R-svglite
Requires: R-viridisLite
Requires: R-webshot
Requires: R-xml2
BuildRequires : R-digest
BuildRequires : R-glue
BuildRequires : R-htmltools
BuildRequires : R-knitr
BuildRequires : R-magrittr
BuildRequires : R-rmarkdown
BuildRequires : R-rstudioapi
BuildRequires : R-rvest
BuildRequires : R-scales
BuildRequires : R-stringr
BuildRequires : R-svglite
BuildRequires : R-viridisLite
BuildRequires : R-webshot
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
and the piping syntax from 'magrittr'. Function 'kable()' is a light weight 
    table generator coming from 'knitr'. This package simplifies the way to 
    manipulate the HTML or 'LaTeX' codes generated by 'kable()' and allows 
    users to construct complex tables and customize styles using a readable 
    syntax.

%prep
%setup -q -c -n kableExtra
cd %{_builddir}/kableExtra

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615231874

%install
export SOURCE_DATE_EPOCH=1615231874
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library kableExtra
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library kableExtra
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library kableExtra
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc kableExtra || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/kableExtra/CODE_OF_CONDUCT.md
/usr/lib64/R/library/kableExtra/CONTRIBUTING.md
/usr/lib64/R/library/kableExtra/DESCRIPTION
/usr/lib64/R/library/kableExtra/INDEX
/usr/lib64/R/library/kableExtra/LICENSE
/usr/lib64/R/library/kableExtra/Meta/Rd.rds
/usr/lib64/R/library/kableExtra/Meta/features.rds
/usr/lib64/R/library/kableExtra/Meta/hsearch.rds
/usr/lib64/R/library/kableExtra/Meta/links.rds
/usr/lib64/R/library/kableExtra/Meta/nsInfo.rds
/usr/lib64/R/library/kableExtra/Meta/package.rds
/usr/lib64/R/library/kableExtra/Meta/vignette.rds
/usr/lib64/R/library/kableExtra/NAMESPACE
/usr/lib64/R/library/kableExtra/NEWS.md
/usr/lib64/R/library/kableExtra/R/kableExtra
/usr/lib64/R/library/kableExtra/R/kableExtra.rdb
/usr/lib64/R/library/kableExtra/R/kableExtra.rdx
/usr/lib64/R/library/kableExtra/bootstrapTable-3.3.7/bootstrapTable.js
/usr/lib64/R/library/kableExtra/bootstrapTable-3.3.7/bootstrapTable.min.css
/usr/lib64/R/library/kableExtra/doc/awesome_table_in_html.R
/usr/lib64/R/library/kableExtra/doc/awesome_table_in_html.Rmd
/usr/lib64/R/library/kableExtra/doc/awesome_table_in_html.html
/usr/lib64/R/library/kableExtra/doc/awesome_table_in_pdf.R
/usr/lib64/R/library/kableExtra/doc/awesome_table_in_pdf.Rmd
/usr/lib64/R/library/kableExtra/doc/awesome_table_in_pdf.pdf
/usr/lib64/R/library/kableExtra/doc/best_practice_for_newline_in_latex_table.R
/usr/lib64/R/library/kableExtra/doc/best_practice_for_newline_in_latex_table.Rmd
/usr/lib64/R/library/kableExtra/doc/best_practice_for_newline_in_latex_table.pdf
/usr/lib64/R/library/kableExtra/doc/index.html
/usr/lib64/R/library/kableExtra/doc/legacy_features.R
/usr/lib64/R/library/kableExtra/doc/legacy_features.Rmd
/usr/lib64/R/library/kableExtra/doc/legacy_features.html
/usr/lib64/R/library/kableExtra/doc/use_kable_in_shiny.R
/usr/lib64/R/library/kableExtra/doc/use_kable_in_shiny.Rmd
/usr/lib64/R/library/kableExtra/doc/use_kable_in_shiny.html
/usr/lib64/R/library/kableExtra/help/AnIndex
/usr/lib64/R/library/kableExtra/help/aliases.rds
/usr/lib64/R/library/kableExtra/help/kableExtra.rdb
/usr/lib64/R/library/kableExtra/help/kableExtra.rdx
/usr/lib64/R/library/kableExtra/help/paths.rds
/usr/lib64/R/library/kableExtra/html/00Index.html
/usr/lib64/R/library/kableExtra/html/R.css
/usr/lib64/R/library/kableExtra/kePrint-0.0.1/kePrint.js
/usr/lib64/R/library/kableExtra/lightable-0.0.1/lightable.css
/usr/lib64/R/library/kableExtra/symbol_index.csv
