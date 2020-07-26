// nthTenlyPrime(n)
// We will say that a number is  (a made-up term) if the digits of the
// number add up to 10. So 1153 is tenly, but 153 is not. With this in mind, write
// the function nthTenlyPrime(n) that takes a non-negative int n and returns the
// nth number that is both tenly and prime. You should also write all the required
// helper functions. The first several tenly primes are: 19, 37, 73, 109, 127…


class nthtenlyprime {
	public boolean istentlyprime(int a){
		int ans = 0;
		int s = 0;
		while(a>0){
			s = a%10;
			ans = ans + s;
			a= a/10;
		}
		if(ans%10==0){
			return true;
		}
		return false;

	}
	public int fun_nthtenlyprime(int n){
		if(n == 1){
			return 19;
		}
		int start = 20;
		int k =2;
		while(true){
			if(istentlyprime(start) == true){
				if(k == n){
					return start;
				}
				k = k + 1;
			}
			start = start + 1;
		}
	}
}