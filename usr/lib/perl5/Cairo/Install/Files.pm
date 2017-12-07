package Cairo::Install::Files;

$self = {
          'inc' => '-I. -Ibuild -DPNG_NO_MMX_CODE -I/usr/include/cairo -I/usr/include/freetype2 -I/usr/include/libpng12  ',
          'typemaps' => [
                          'cairo-perl-auto.typemap',
                          'cairo-perl.typemap'
                        ],
          'deps' => [],
          'libs' => '-lcairo  '
        };


# this is for backwards compatiblity
@deps = @{ $self->{deps} };
@typemaps = @{ $self->{typemaps} };
$libs = $self->{libs};
$inc = $self->{inc};

	$CORE = undef;
	foreach (@INC) {
		if ( -f $_ . "/Cairo/Install/Files.pm") {
			$CORE = $_ . "/Cairo/Install/";
			last;
		}
	}

1;
