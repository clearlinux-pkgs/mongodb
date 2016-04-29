#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mongodb
Version  : 3.2.1
Release  : 16
URL      : https://github.com/mongodb/mongo/archive/r3.2.1.tar.gz
Source0  : https://github.com/mongodb/mongo/archive/r3.2.1.tar.gz
Source1  : mongodb.service
Source2  : mongodb.tmpfiles
Summary  : MongoDB open source document-oriented database system (metapackage)
Group    : Development/Tools
License  : AGPL-3.0 Apache-2.0 BSD-3-Clause BSD-3-Clause-Clear BSL-1.0 GPL-2.0 MIT OpenSSL
Requires: mongodb-bin
Requires: mongodb-config
BuildRequires : boost-dev
BuildRequires : gcc-dev
BuildRequires : gperftools-dev
BuildRequires : openssl-dev
BuildRequires : pbr
BuildRequires : pcre-dev
BuildRequires : pcre-extras
BuildRequires : pip
BuildRequires : pkgconfig(valgrind)
BuildRequires : python-dev
BuildRequires : scons
BuildRequires : setuptools
BuildRequires : snappy-dev
BuildRequires : wiredtiger-dev
BuildRequires : yaml-cpp-dev
BuildRequires : zlib-dev
Patch1: 0001-point-to-_bindir.patch
Patch2: 0002-ignore-config-enoent.patch
Patch3: 0003-Change-default-dbpath.patch
Patch4: 0004-Set-default-bind-ip-to-127.0.0.1.patch
Patch5: 0005-version.json.patch

%description
MongoDB is built for scalability, performance and high availability, scaling from single server deployments to large, complex multi-site architectures. By leveraging in-memory computing, MongoDB provides high performance for both reads and writes. MongoDBâs native replication and automated failover enable enterprise-grade reliability and operational flexibility.

MongoDB is an open-source database used by companies of all sizes, across all industries and for a wide variety of applications. It is an agile database that allows schemas to change quickly as applications evolve, while still providing the functionality developers expect from traditional databases, such as secondary indexes, a full query language and strict consistency.

MongoDB has a rich client ecosystem including hadoop integration, officially supported drivers for 10 programming languages and environments, as well as 40 drivers supported by the user community.

MongoDB features:
* JSON Data Model with Dynamic Schemas
* Auto-Sharding for Horizontal Scalability
* Built-In Replication for High Availability
* Rich Secondary Indexes, including geospatial
* TTL indexes
* Text Search
* Aggregation Framework & Native MapReduce

This metapackage will install the mongo shell, import/export tools, other client utilities, server software, default configuration, and init.d scripts.

%package bin
Summary: bin components for the mongodb package.
Group: Binaries
Requires: mongodb-config

%description bin
bin components for the mongodb package.


%package config
Summary: config components for the mongodb package.
Group: Default

%description config
config components for the mongodb package.


%prep
%setup -q -n mongo-r3.2.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
scons %{?_smp_mflags}  all \
--disable-warnings-as-errors \
--prefix=%{buildroot}%{_prefix} \
--ssl \
--use-system-tcmalloc \
--use-system-boost \
--use-system-pcre \
--use-system-snappy \
--use-system-zlib \
--use-system-yaml \
--use-system-valgrind \
--use-system-wiredtiger

%install
scons install %{?_smp_mflags} --disable-warnings-as-errors --prefix=%{buildroot}%{_prefix} --ssl --use-system-tcmalloc --use-system-boost --use-system-pcre --use-system-snappy --use-system-zlib --use-system-yaml --use-system-valgrind --use-system-wiredtiger
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/mongodb.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/tmpfiles.d/mongodb.conf

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mongo
/usr/bin/mongod
/usr/bin/mongoperf
/usr/bin/mongos

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/mongodb.service
/usr/lib/tmpfiles.d/mongodb.conf
