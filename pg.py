#coding: utf-8

import gnupg
import os
import subprocess

class SimpleGPG(object):
    u"""
        Let sign files via gnupg
    """
    # folder store keys
    KEY_DIR = 'keys'
    # binary to run all stuff used by gnupg wrapper
    GPG_BINARY = '..\GnuPG\pub\gpg.exe'
    ENCRYPTED_FILE = 'encrypted'
    DECRYPTED_FILE = 'decrypted'
    SIGN_FILE = 'signed.txt.sig'
    
    def __init__(self):
        self.gpg = gnupg.GPG(gnupghome=self.KEY_DIR, gpgbinary=self.GPG_BINARY)
        self.signer_fingerprint = ''
        self.reciever_fingerprint = ''
        self.passphrase = 'qwrety'
        self.find_keys()

    def log(self, msg):
        print msg

    def find_keys(self):
        pubring_path = os.path.join(self.KEY_DIR, 'pubring.gpg')
        secring_path = os.path.join(self.KEY_DIR, 'secring.gpg')
        if os.path.exists(pubring_path) and os.path.exists(secring_path):
            self.log('loading keys')
            self.signer_fingerprint = self.gpg.import_keys(open(secring_path, 'rb').read()).fingerprints[0]
            self.reciever_fingerprint = self.gpg.import_keys(open(pubring_path, 'rb').read()).fingerprints[1]
            self.log('loaded keys')
            self.log(self.signer_fingerprint)
            self.log(self.reciever_fingerprint)
        else:
            # If needed generate keys else use existing
            key = self._generate_key("UserName", "UserFName", "usersite.com")
            self.signer_fingerprint = key.fingerprint
            key = self._generate_key( "Barbara", "Brown", "beta.com")
            self.reciever_fingerprint = key.fingerprint

    def _generate_key(self, first_name, last_name, domain, passphrase=None):
        u""" Generate a key"""
        params = {
            'Key-Type': 'RSA',
            'Key-Length': 1024,
            'Subkey-Type': 'ELG-E',
            'Subkey-Length': 2048,
            'Name-Comment': 'A test user',
        }
        params['Name-Real'] = '%s %s' % (first_name, last_name)
        params['Name-Email'] = ("%s.%s@%s" % (first_name, last_name, domain)).lower()
        if passphrase is not None:
			self.passphrase = passphrase
 
        params['Passphrase'] = self.passphrase

        self.log('generating keys')
        cmd = self.gpg.gen_key_input(**params)
        key = self.gpg.gen_key(cmd)
        self.log('done generate')

        return key

    def encrypt(self, file_):
        self.save_remove_file(self.ENCRYPTED_FILE)
        encrypted = self.gpg.encrypt_file(
            open(file_, 'rb'),
            self.reciever_fingerprint,
            sign=self.signer_fingerprint,
            passphrase=self.passphrase,
            output=self.ENCRYPTED_FILE)

        assert encrypted.status is not None
        return os.path.exists(self.ENCRYPTED_FILE)

    def decrypt(self):
        # Data is in encrypted.txt. Read it in and verify/decrypt it.
        res = False
        if os.path.exists(self.ENCRYPTED_FILE):
            data = open(self.ENCRYPTED_FILE, 'r').read()
            self.save_remove_file(self.DECRYPTED_FILE)
            decrypted = self.gpg.decrypt(data, passphrase=self.passphrase,
                                         output=self.DECRYPTED_FILE)
            #self.print_info(decrypted)
            res = True
        return res

    def sign(self, f):
        d = self.gpg.sign_file(open(f, 'r'))
        self.log('had signed message. result:\n %s'%d.data)
        resf = open(self.SIGN_FILE, 'w')
        resf.writelines(d.data)
        return d.data
        #subprocess.call(u'gpg --passphrase %s --clearsign --detach-sign -a 1.txt '%(self.passphrase), shell=True)

    def save_remove_file(self, f):
        if os.path.isfile(f):
            os.remove(f)

    def print_info(decrypted):
        print('User name: %s' % decrypted.username)
        print('Key id: %s' % decrypted.key_id)
        print('Signature id: %s' % decrypted.signature_id)
        print('Signature timestamp: %s' % decrypted.sig_timestamp)
        print('Fingerprint: %s' % decrypted.fingerprint)


if __name__ == '__main__':
    gpg_work = SimpleGPG()
