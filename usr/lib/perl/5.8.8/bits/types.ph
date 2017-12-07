require '_h2ph_pre.ph';

no warnings 'redefine';

unless(defined(&_BITS_TYPES_H)) {
    eval 'sub _BITS_TYPES_H () {1;}' unless defined(&_BITS_TYPES_H);
    require 'features.ph';
    require 'bits/wordsize.ph';
    eval 'sub __need_size_t () {1;}' unless defined(&__need_size_t);
    require 'stddef.ph';
    if((defined(&__WORDSIZE) ? &__WORDSIZE : undef) == 64) {
    }
 elsif(defined (defined(&__GLIBC_HAVE_LONG_LONG) ? &__GLIBC_HAVE_LONG_LONG : undef)) {
    }
    if((defined(&__WORDSIZE) ? &__WORDSIZE : undef) == 64) {
    }
 elsif(defined (defined(&__GLIBC_HAVE_LONG_LONG) ? &__GLIBC_HAVE_LONG_LONG : undef)) {
    } else {
    }
    eval 'sub __S16_TYPE () {\'short int\';}' unless defined(&__S16_TYPE);
    eval 'sub __U16_TYPE () {\'unsigned short int\';}' unless defined(&__U16_TYPE);
    eval 'sub __S32_TYPE () {\'int\';}' unless defined(&__S32_TYPE);
    eval 'sub __U32_TYPE () {\'unsigned int\';}' unless defined(&__U32_TYPE);
    eval 'sub __SLONGWORD_TYPE () {\'long int\';}' unless defined(&__SLONGWORD_TYPE);
    eval 'sub __ULONGWORD_TYPE () {\'unsigned long int\';}' unless defined(&__ULONGWORD_TYPE);
    if((defined(&__WORDSIZE) ? &__WORDSIZE : undef) == 32) {
	eval 'sub __SQUAD_TYPE () { &__quad_t;}' unless defined(&__SQUAD_TYPE);
	eval 'sub __UQUAD_TYPE () { &__u_quad_t;}' unless defined(&__UQUAD_TYPE);
	eval 'sub __SWORD_TYPE () {\'int\';}' unless defined(&__SWORD_TYPE);
	eval 'sub __UWORD_TYPE () {\'unsigned int\';}' unless defined(&__UWORD_TYPE);
	eval 'sub __SLONG32_TYPE () {\'long int\';}' unless defined(&__SLONG32_TYPE);
	eval 'sub __ULONG32_TYPE () {\'unsigned long int\';}' unless defined(&__ULONG32_TYPE);
	eval 'sub __S64_TYPE () { &__quad_t;}' unless defined(&__S64_TYPE);
	eval 'sub __U64_TYPE () { &__u_quad_t;}' unless defined(&__U64_TYPE);
	eval 'sub __STD_TYPE () { &__extension__  &typedef;}' unless defined(&__STD_TYPE);
    }
 elsif((defined(&__WORDSIZE) ? &__WORDSIZE : undef) == 64) {
	eval 'sub __SQUAD_TYPE () {\'long int\';}' unless defined(&__SQUAD_TYPE);
	eval 'sub __UQUAD_TYPE () {\'unsigned long int\';}' unless defined(&__UQUAD_TYPE);
	eval 'sub __SWORD_TYPE () {\'long int\';}' unless defined(&__SWORD_TYPE);
	eval 'sub __UWORD_TYPE () {\'unsigned long int\';}' unless defined(&__UWORD_TYPE);
	eval 'sub __SLONG32_TYPE () {\'int\';}' unless defined(&__SLONG32_TYPE);
	eval 'sub __ULONG32_TYPE () {\'unsigned int\';}' unless defined(&__ULONG32_TYPE);
	eval 'sub __S64_TYPE () {\'long int\';}' unless defined(&__S64_TYPE);
	eval 'sub __U64_TYPE () {\'unsigned long int\';}' unless defined(&__U64_TYPE);
	eval 'sub __STD_TYPE () { &typedef;}' unless defined(&__STD_TYPE);
    } else {
    }
    require 'bits/typesizes.ph';
    undef(&__STD_TYPE) if defined(&__STD_TYPE);
}
1;