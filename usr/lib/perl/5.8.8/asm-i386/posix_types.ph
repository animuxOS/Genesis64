require '_h2ph_pre.ph';

no warnings 'redefine';

unless(defined(&__ARCH_I386_POSIX_TYPES_H)) {
    eval 'sub __ARCH_I386_POSIX_TYPES_H () {1;}' unless defined(&__ARCH_I386_POSIX_TYPES_H);
    if(defined(&__GNUC__)) {
    }
    if(defined( &__KERNEL__) || defined( &__USE_ALL)) {
    } else {
    }
    if(defined( &__KERNEL__) || !defined( &__GLIBC__) || ((defined(&__GLIBC__) ? &__GLIBC__ : undef) < 2)) {
	undef(&__FD_SET) if defined(&__FD_SET);
	eval 'sub __FD_SET {
	    my($fd,$fdsetp) = @_;
    	    eval q(\\"(assembly code)\\");
	}' unless defined(&__FD_SET);
	undef(&__FD_CLR) if defined(&__FD_CLR);
	eval 'sub __FD_CLR {
	    my($fd,$fdsetp) = @_;
    	    eval q(\\"(assembly code)\\");
	}' unless defined(&__FD_CLR);
	undef(&__FD_ISSET) if defined(&__FD_ISSET);
	eval 'sub __FD_ISSET {
	    my($fd,$fdsetp) = @_;
    	    eval q(\\"(assembly code)\\");
	}' unless defined(&__FD_ISSET);
	undef(&__FD_ZERO) if defined(&__FD_ZERO);
	eval 'sub __FD_ZERO {
	    my($fdsetp) = @_;
    	    eval q(\\"(assembly code)\\");
	}' unless defined(&__FD_ZERO);
    }
}
1;
