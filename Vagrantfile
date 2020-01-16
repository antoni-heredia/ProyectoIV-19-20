Vagrant.configure("2") do |config|
    #Nombre
    config.vm.define "WallyFinder"

    # Aunque la versión mas usada es ubuntu/trusty64, que es la 14.04, he decidido usar 
    # 18.04 porque todo mi sistema esta probado en esa versión
    config.vm.box = "ubuntu/bionic64"
   

    # Usamos la dirección ip local con el puerto 1234 tanto en el anfitrión como en el invitado
    config.vm.network "forwarded_port", guest: 1234, host: 1234, host_ip: "127.0.0.1"

    #Para evitar actualizaciones automaticas
    config.vm.box_check_update = false

    # Vamos a usar virtualbox de forma local 
    config.vm.provider "virtualbox" do |vb|
        #El nombre de la maquina
        vb.name = "WallyFinder"
        #La cantidad de memoria ram que tendra disponible. En mi caso 2GB
        vb.memory = "2048"
        #Y podra usar dos cores del procesador
        vb.cpus = 2
    end

    # Indicaremos que el aprovisionamiento lo realizara con el fichero de ansible
    # que se encuentra en la siguiente ruta
    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "aprovisionamiento/playbook.yml"
    end
end