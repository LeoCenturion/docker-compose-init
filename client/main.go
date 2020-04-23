package main

import (
	"log"
	"time"

	"github.com/pkg/errors"
	"github.com/spf13/viper"

	"github.com/7574-sistemas-distribuidos/docker-compose-init/client/common"
)

// InitConfig Function that uses viper library to parse env variables. If
// some of the variables cannot be parsed, an error is returned
func InitConfigEnv() (*viper.Viper, error) {
	v := viper.New()

	// Configure viper to read env variables with the CLI_ prefix
	v.AutomaticEnv()
	v.SetEnvPrefix("cli")

	// Add env variables supported
	v.BindEnv("id")
	v.BindEnv("server", "address")
	v.BindEnv("loop", "period")
	v.BindEnv("loop", "lapse")

	//config file
	v.SetConfigName("config.yaml")
	v.SetConfigType("yaml")
	v.AddConfigPath("/config/")
	v.ReadInConfig()

	// Parse time.Duration variables and return an error
	// if those variables cannot be parsed
	if _, err := time.ParseDuration(v.GetString("loop_lapse")); err != nil {
		return nil, errors.Wrapf(err, "Could not parse CLI_LOOP_LAPSE env var as time.Duration.")
	}

	if _, err := time.ParseDuration(v.GetString("loop_period")); err != nil {
		return nil, errors.Wrapf(err, "Could not parse CLI_LOOP_PERIOD env var as time.Duration.")
	}

	return v, nil
}


func main() {
	config, config_err := InitConfigEnv()
	if config_err != nil {
		log.Fatalf("%s", config_err)
	}

	clientConfig := common.ClientConfig{
		ServerAddress: config.GetString("server_address"),
		ID:            config.GetString("id"),
		LoopLapse:     config.GetDuration("loop_lapse"),
		LoopPeriod:    config.GetDuration("loop_period"),
	}

	client := common.NewClient(clientConfig)
	client.StartClientLoop()
}
