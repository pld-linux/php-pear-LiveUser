%include	/usr/lib/rpm/macros.php
%define		_class		LiveUser
%define		_status		beta
%define		_pearname	%{_class}

Summary:	%{_pearname} - User authentication and permission management framework
Summary(pl):	%{_pearname} - Uwierzytelnianie u¿ytkowników i zarz±dzanie uprawnieniami
Name:		php-pear-%{_pearname}
Version:	0.10.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	81698911e39b4d27274e2bd559d77419
URL:		http://pear.php.net/package/LiveUser/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perm_LiveUser is a set of classes for dealing with user authentication
and permission management. Basically, there are three main elements
that make up this package:
- The LoginManager,
- The Auth containers,
- The Perm containers.

The LoginManager class takes care of the login process and can be
configured to use a certain permission container and one or more
different auth containers. That means, you can have your users' data
scattered amongst many data containers and have the LoginManager try
each defined container until the user is found. For example, you can
have all website users who can apply for a new account online on the
webserver's local database. Also, you want to enable all your
company's employees to login to the site without the need to create
new accounts for all of them. To achieve that, a second container can
be defined to be used by the LoginManager. You can also define a
permission container of your choice that will manage the rights for
each user. Depending on the container, you can implement any kind of
permission schemes for your application while having one consistent
API. Using different permission and auth containers, it's easily
possible to integrate newly written applications with older ones that
have their own ways of storing permissions and user data. Just make a
new container type and you're ready to go! Currently available are
RDBMS containers using PEAR::DB. More are soon to follow.

This class has in PEAR status: %{_status}.

%description -l pl
Perm_LiveUser to zestaw klas do uwierzytelniania u¿ytkowników i
zarz±dzania uprawnieniami. Zasadniczo na ten pakiet sk³adaj± siê trzy
g³ówne elementy:
- LoginManager (zarz±dca logowania),
- kontenery Auth (uwierzytelniania),
- kontenery Perm (uprawnieñ.

Klasa LoginManager obs³uguje proces logowania i mo¿e byæ
skonfigurowana do u¿ywania ró¿nych kontenerów uprawnieñ oraz jednego
lub wiêkszej liczby kontenerów uwierzytelniania. Oznacza to, ¿e mo¿na
mieæ dane u¿ytkowników rozproszone po ró¿nych kontenerach danych, a
LoginManager bêdzie próbowa³ u¿yæ ka¿dego zdefiniowanego kontenera a¿
do znalezienia u¿ytkownika. Na przyk³ad mo¿na mieæ wszystkich
u¿ytkowników strony WWW, którzy mog± zg³osiæ siê po nowe konto ze
strony do lokalnej bazy danych serwera WWW. Mo¿na te¿ chcieæ umo¿liwiæ
wszystkim pracownikom firmy na logowanie do strony bez potrzeby
tworzenia im nowych kont. Aby to osi±gn±æ, mo¿na zdefiniowaæ drugi
kontener dla LoginManagera. Mo¿na tak¿e zdefiniowaæ kontener
uprawnieñ, który bêdzie zarz±dza³ prawami dla ka¿dego u¿ytkownika.
Zale¿nie od kontenera mo¿na zaimplementowaæ dowolne rodzaje schematów
uprawnieñ dla aplikacji ca³y czas maj±c jedno spójne API. Przy u¿yciu
ró¿nych kontenerów uprawnieñ i uwierzytelniania mo¿na ³atwo
zintegrowaæ nowo pisane aplikacje ze starszymi, które mia³y w³asne
sposoby zapisywania uprawnieñ i danych u¿ytkowników - wystarczy
stworzyæ nowy typ kontenera. Aktualnie dostêpne s± kontenery RDBMS
u¿ywaj±ce PEAR::DB, wkrótce bêdzie wiêcej.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{Admin,Auth,Perm}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}
install %{_pearname}-%{version}/Admin/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Admin
install %{_pearname}-%{version}/Auth/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Auth
install %{_pearname}-%{version}/Perm/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Perm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{docs,scripts,sql}
%{php_pear_dir}/%{_class}.php
%{php_pear_dir}/%{_class}
