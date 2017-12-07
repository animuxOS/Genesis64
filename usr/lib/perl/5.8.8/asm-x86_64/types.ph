require '_h2ph_pre.ph';

no warnings 'redefine';

unless(defined(&_X86_64_TYPES_H)) {
    eval 'sub _X86_64_TYPES_H () {1;}' unless defined(&_X86_64_TYPES_H);
    unless(defined(&__ASSEMBLY__)) {
    }
}
1;
