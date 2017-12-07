require '_h2ph_pre.ph';

no warnings 'redefine';

unless(defined(&_ASM_X86_64_POSIX_TYPES_H)) {
    eval 'sub _ASM_X86_64_POSIX_TYPES_H () {1;}' unless defined(&_ASM_X86_64_POSIX_TYPES_H);
    if(defined(&__GNUC__)) {
    }
}
1;
