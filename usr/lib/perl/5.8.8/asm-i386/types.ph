require '_h2ph_pre.ph';

no warnings 'redefine';

unless(defined(&_I386_TYPES_H)) {
    eval 'sub _I386_TYPES_H () {1;}' unless defined(&_I386_TYPES_H);
    unless(defined(&__ASSEMBLY__)) {
	if(defined( &__GNUC__)  && !defined( &__STRICT_ANSI__)) {
	}
    }
}
1;
