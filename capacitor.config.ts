import type { CapacitorConfig } from '@capacitor/cli'

const config: CapacitorConfig = {
  appId: 'com.novafleet.android',
  appName: 'Midas Yazıcı Kontrol',
  webDir: 'dist',
  android: {
    allowMixedContent: true,
  },
}

export default config
