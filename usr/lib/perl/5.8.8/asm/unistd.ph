require '_h2ph_pre.ph';

no warnings 'redefine';

unless(defined(&__ASM_STUB_UNISTD_H)) {
    eval 'sub __ASM_STUB_UNISTD_H () {1;}' unless defined(&__ASM_STUB_UNISTD_H);
    if(defined (defined(&__x86_64__) ? &__x86_64__ : undef)) {
	require 'asm-x86_64/unistd.ph';
    }
 elsif(defined (defined(&__i386__) ? &__i386__ : undef)) {
	require 'asm-i386/unistd.ph';
    } else {
	warn("This\ machine\ appears\ to\ be\ neither\ x86_64\ nor\ i386\.");
    }
}
1;
