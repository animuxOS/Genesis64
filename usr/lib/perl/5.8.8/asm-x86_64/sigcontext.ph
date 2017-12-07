require '_h2ph_pre.ph';

no warnings 'redefine';

unless(defined(&_ASM_X86_64_SIGCONTEXT_H)) {
    eval 'sub _ASM_X86_64_SIGCONTEXT_H () {1;}' unless defined(&_ASM_X86_64_SIGCONTEXT_H);
    require 'asm/types.ph';
}
1;
